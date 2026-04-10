from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from miscellaneous.models import Blog, BlogCategory, BlogTag
from products.models import Product, ProductCategory, ProductType
from public_panel.permissions import UserLoginCheckRequiredMixin, UserLoginRequiredMixin, user_login_required
from user_items.models import CartItem, Wishlist
from users.models import User
from django.db import models

class LoginPageView(UserLoginCheckRequiredMixin, generic.TemplateView):
    template_name = "public-panel/login.html"
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == "user":
            login(request, user)
            return redirect("admin-home-page")
        else:
            context = self.get_context_data()
            if user:
                context["error"] = "Invalid credentials, admin are not allowed here."
            else:
                context["error"] = "Invalid credentials"
            return self.render_to_response(context)


class LogoutView(generic.TemplateView):
    template_name = "public-panel/logout.html"

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("login-page")


class RegisterPageView(UserLoginCheckRequiredMixin, generic.TemplateView):
    template_name = "public-panel/register.html"
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if not all([username, password, email, first_name, last_name]):
            context = self.get_context_data()
            context["error"] = "All fields are required."
            return self.render_to_response(context)

        if User.objects.filter(username=username).exists():
            context = self.get_context_data()
            context["error"] = "Username already exists."
            return self.render_to_response(context)

        User.objects.create(
            username=username, 
            password=make_password(password), 
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
        )
        return redirect("login-page")

class HomePageView(generic.TemplateView):
    template_name = "public-panel/index.html"

class AboutPageView(generic.TemplateView):
    template_name = "public-panel/about.html"


class CartPageView(UserLoginRequiredMixin, generic.ListView):
    template_name = "public-panel/cart.html"
    
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user).annotate(
            subtotal=models.F('quantity') * models.F('product__price')
        )

class DashboardPageView(UserLoginRequiredMixin, generic.TemplateView):
    template_name = "public-panel/dashboard/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add user to context (already available as request.user)
        context['user'] = self.request.user
        
        # TODO: Add cart items when Cart model is created
        # context['cart_items'] = Cart.objects.filter(user=self.request.user)
        # context['cart_total'] = sum(item.subtotal for item in context['cart_items'])
        context['cart_items'] = CartItem.objects.filter(user=self.request.user).annotate(
            subtotal=models.F('quantity') * models.F('product__price')
        )
        context['cart_total'] = CartItem.objects.filter(user=self.request.user).aggregate(
            total=models.Sum(models.F('quantity') * models.F('product__price'))
        )['total'] or 0
        
        # TODO: Add orders when Order model is created
        # context['orders'] = Order.objects.filter(user=self.request.user).order_by('-created_at')
        context['orders'] = []
        
        # TODO: Add wishlist items when Wishlist model is created
        # context['wishlist_items'] = Wishlist.objects.filter(user=self.request.user)
        context['wishlist_items'] =  Wishlist.objects.filter(user=self.request.user)
        
        return context
    
class CategoryPageView(generic.ListView):
    template_name = "public-panel/category.html"
    queryset = ProductCategory.objects.all()
    context_object_name = "categories" # object_list by default, changed to categories for clarity

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = ProductCategory.objects.all()
    #     return context
    
class ProductListPageView(generic.ListView):
    template_name = "public-panel/product-list.html"
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context.update(
            categories = ProductCategory.objects.all(),
            types = ProductType.objects.all(),
        )
        return context
    
class ProductDetailPageView(generic.DetailView):
    template_name = "public-panel/product-detail.html"
    queryset = Product.objects.all() # Change to Product.objects.all() when Product model is created
    context_object_name = "product"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = ProductCategory.objects.all()
    #     return context


class BlogListPageView(generic.ListView):
    template_name = "public-panel/blog.html"
    queryset = Blog.objects.all()
    # object_list
    context_object_name = "blogs"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context.update(
            categories = BlogCategory.objects.all(),
            tags = BlogTag.objects.all(),
            recent_blogs = Blog.objects.order_by('-created_at')[:4],
        )
        return context
    
class BlogDetailPageView(generic.DetailView):
    template_name = "public-panel/blog-detail.html"
    queryset = Blog.objects.all()
    # object
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context.update(
            categories = BlogCategory.objects.all(),
            tags = BlogTag.objects.all(),
            recent_blogs = Blog.objects.order_by('-created_at')[:4],
        )
        return context
    

from django.http import JsonResponse

@user_login_required
def add_to_wishlist(request, product_id, action):
    if action not in ["add", "remove"]:
        response = JsonResponse({"message": "Invalid action. Use 'add' or 'remove'."})
        response.status_code = 400
        return response
    
    products = Product.objects.filter(pk=product_id) 

    if products.exists():
        product = products.first()
        
        if action == "remove":
            wls = Wishlist.objects.filter(user=request.user, product=product)
            if wls.exists():
                wl = wls.first()
                wl.delete()
                message = {"message": f"Product #{product_id} removed from wishlist successfully."}
                status = 200
            else:
                message = {"message": f"Product #{product_id} is not in your wishlist."}
                status = 400
        else:
            _, created = Wishlist.objects.get_or_create(user=request.user, product=product)
            if created:
                message = {"message": f"Product #{product_id} added to wishlist successfully."}
            else:
                message = {"message": f"Product #{product_id} is already in your wishlist."}
            
            status = 200
    else:
        message= {"message": f"Product not added to wishlist, since it does not exist!"}
        status = 400

    response = JsonResponse(message)
    response.status_code = status
    return response

@user_login_required
def add_to_cart(request):
    if request.method != "POST":
        response = JsonResponse({"message": "Invalid request method. Use POST."})
        response.status_code = 400
        return response

    data = request.POST

    user = request.user
    product = data.get("product")
    quantity = data.get("quantity", "0") # Remove Action if qty = 0 else update / add cart qty
    quantity = int(quantity)

    if quantity == 0:
        deleted_items,_ = CartItem.objects.filter(
        user=user,
        product_id=product).delete()

        if deleted_items > 0:
            message = {"message": f"Product #{product} removed from cart successfully."}
            status = 200
        else:
            message = {"message": f"Product #{product} is not in your cart."}
            status = 400
    else:
        _, flag =  CartItem.objects.update_or_create(
            user=user,
            product_id=product,
            defaults={"quantity": quantity}
        )
        if flag:
            message = {"message": f"Product #{product} added to cart successfully."}
        else:
            message = {"message": f"Product #{product} quantity updated in cart successfully."}

        status = 200
    
    response = JsonResponse(message)
    response.status_code = status
    return response



# 1xx -> Informational
# 2xx -> Success
# 3xx -> Redirection
# 4xx -> Client Error
# 5xx -> Server Error

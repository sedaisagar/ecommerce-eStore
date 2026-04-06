from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from products.models import Product, ProductCategory, ProductType
from public_panel.permissions import UserLoginCheckRequiredMixin, UserLoginRequiredMixin
from users.models import User

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

class DashboardPageView(UserLoginRequiredMixin, generic.TemplateView):
    template_name = "public-panel/dashboard/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add user to context (already available as request.user)
        context['user'] = self.request.user
        
        # TODO: Add cart items when Cart model is created
        # context['cart_items'] = Cart.objects.filter(user=self.request.user)
        # context['cart_total'] = sum(item.subtotal for item in context['cart_items'])
        context['cart_items'] = []
        context['cart_total'] = 0
        
        # TODO: Add orders when Order model is created
        # context['orders'] = Order.objects.filter(user=self.request.user).order_by('-created_at')
        context['orders'] = []
        
        # TODO: Add wishlist items when Wishlist model is created
        # context['wishlist_items'] = Wishlist.objects.filter(user=self.request.user)
        context['wishlist_items'] = []
        
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
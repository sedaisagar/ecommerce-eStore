from django.views import generic

from admin_panel.permissions import AdminLoginRequiredMixin
from products.models import Product, ProductCategory, ProductType
from django.urls import reverse_lazy

# Product Category Views

class ProductCategoryListView(AdminLoginRequiredMixin, generic.ListView):
    template_name = "admin-panel/commons/list.html"
    queryset = ProductCategory.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Product Categories"
        data["fields"] = ["name"]
        data["actions"] = ["create", "edit", "delete"]
        return data
    
class ProductCategoryCreateView(AdminLoginRequiredMixin, generic.CreateView):
    template_name = "admin-panel/commons/form.html"
    model = ProductCategory
    fields = "__all__"
    success_url = reverse_lazy("admin-product-cat-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Create Product Category"
        return data
    
class ProductCategoryEditView(AdminLoginRequiredMixin, generic.UpdateView):
    template_name = "admin-panel/commons/form.html"
    model = ProductCategory
    fields = "__all__"
    success_url = reverse_lazy("admin-product-cat-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Edit Product Category"
        return data
    
class ProductCategoryDeleteView(AdminLoginRequiredMixin, generic.DeleteView):
    template_name = "admin-panel/commons/form.html"
    model = ProductCategory
    success_url = reverse_lazy("admin-product-cat-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete Product Category"
        return data

# Product Type Views

class ProductTypeListView(AdminLoginRequiredMixin, generic.ListView):
    template_name = "admin-panel/commons/list.html"
    queryset = ProductType.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Product Categories"
        data["fields"] = ["name"]
        data["actions"] = ["create", "edit", "delete"]
        return data
    
class ProductTypeCreateView(AdminLoginRequiredMixin, generic.CreateView):
    template_name = "admin-panel/commons/form.html"
    model = ProductType
    fields = "__all__"
    success_url = reverse_lazy("admin-product-type-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Create Product Type"
        return data
    
class ProductTypeEditView(AdminLoginRequiredMixin, generic.UpdateView):
    template_name = "admin-panel/commons/form.html"
    model = ProductType
    fields = "__all__"
    success_url = reverse_lazy("admin-product-type-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Edit Product Type"
        return data
    
class ProductTypeDeleteView(AdminLoginRequiredMixin, generic.DeleteView):
    template_name = "admin-panel/commons/form.html"
    model = ProductType
    success_url = reverse_lazy("admin-product-type-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete Product Type"
        return data

# Products Views

class ProductsListView(AdminLoginRequiredMixin, generic.ListView):
    template_name = "admin-panel/commons/list.html"
    queryset = Product.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Products"
        data["fields"] = ["name", "price", "category", "type"]
        data["actions"] = ["create", "edit", "delete"]
        return data
    
class ProductsCreateView(AdminLoginRequiredMixin, generic.CreateView):
    template_name = "admin-panel/commons/form.html"
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("admin-product-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Create Product"
        return data
    
class ProductsEditView(AdminLoginRequiredMixin, generic.UpdateView):
    template_name = "admin-panel/commons/form.html"
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("admin-product-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Edit Product"
        return data
    
class ProductsDeleteView(AdminLoginRequiredMixin, generic.DeleteView):
    template_name = "admin-panel/commons/form.html"
    model = Product
    success_url = reverse_lazy("admin-product-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete Product"
        return data

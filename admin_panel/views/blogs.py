from django.views import generic

from admin_panel.permissions import AdminLoginRequiredMixin
from django.urls import reverse_lazy

from miscellaneous.models import Blog, BlogCategory, BlogTag

# Blog Category Views

class BlogCategoryListView(AdminLoginRequiredMixin, generic.ListView):
    template_name = "admin-panel/commons/list.html"
    queryset = BlogCategory.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Blog Categories"
        data["fields"] = ["name"]
        data["actions"] = ["create", "edit", "delete"]
        return data
    
class BlogCategoryCreateView(AdminLoginRequiredMixin, generic.CreateView):
    template_name = "admin-panel/commons/form.html"
    model = BlogCategory
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-cat-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Create Blog Category"
        return data
    
class BlogCategoryEditView(AdminLoginRequiredMixin, generic.UpdateView):
    template_name = "admin-panel/commons/form.html"
    model = BlogCategory
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-cat-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Edit Blog Category"
        return data
    
class BlogCategoryDeleteView(AdminLoginRequiredMixin, generic.DeleteView):
    template_name = "admin-panel/commons/form.html"
    model = BlogCategory
    success_url = reverse_lazy("admin-blog-cat-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete Blog Category"
        return data

# Blog Tag Views

class BlogTagListView(AdminLoginRequiredMixin, generic.ListView):
    template_name = "admin-panel/commons/list.html"
    queryset = BlogTag.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Blog Tags"
        data["fields"] = ["name"]
        data["actions"] = ["create", "edit", "delete"]
        return data
    
class BlogTagCreateView(AdminLoginRequiredMixin, generic.CreateView):
    template_name = "admin-panel/commons/form.html"
    model = BlogTag
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-tag-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Create Blog Tag"
        return data
    
class BlogTagEditView(AdminLoginRequiredMixin, generic.UpdateView):
    template_name = "admin-panel/commons/form.html"
    model = BlogTag
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-tag-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Edit Blog Tag"
        return data
    
class BlogTagDeleteView(AdminLoginRequiredMixin, generic.DeleteView):
    template_name = "admin-panel/commons/form.html"
    model = BlogTag
    success_url = reverse_lazy("admin-blog-tag-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete Blog Tag"
        return data

# Products Views
from tinymce.widgets import TinyMCE
class BlogListView(AdminLoginRequiredMixin, generic.ListView):
    template_name = "admin-panel/commons/list.html"
    queryset = Blog.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Blogs"
        data["fields"] = ["category", "title"]
        data["actions"] = ["create", "edit", "delete"]
        return data
    
class BlogCreateView(AdminLoginRequiredMixin, generic.CreateView):
    template_name = "admin-panel/commons/form.html"
    model = Blog
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Create Blog"
        return data
    
    def get_form(self):
        form = super().get_form()
        form.fields['description'].widget = TinyMCE(attrs={'cols': 80, 'rows': 30})
        return form
    
class BlogEditView(AdminLoginRequiredMixin, generic.UpdateView):
    template_name = "admin-panel/commons/form.html"
    model = Blog
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Edit Blog"
        return data
    
    def get_form(self):
        form = super().get_form()
        form.fields['description'].widget = TinyMCE(attrs={'cols': 80, 'rows': 30})
        return form

class BlogDeleteView(AdminLoginRequiredMixin, generic.DeleteView):
    template_name = "admin-panel/commons/form.html"
    model = Blog
    success_url = reverse_lazy("admin-blog-list")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete Blog"
        return data

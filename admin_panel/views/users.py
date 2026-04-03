from django.views import generic

from admin_panel.permissions import AdminLoginRequiredMixin
from users.models import User

class AdminAdminListView(AdminLoginRequiredMixin, generic.ListView):
    template_name = "admin-panel/commons/list.html"
    queryset = User.objects.filter(role = "admin")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Admin Users"
        data["fields"] = ["username", "role", "email"]
        data["actions"] = []
        return data

class AdminUserListView(AdminLoginRequiredMixin, generic.ListView):
    template_name = "admin-panel/commons/list.html"
    queryset = User.objects.filter(role = "user")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Admin Users"
        data["fields"] = ["username", "role", "email"]
        data["actions"] = []
        return data
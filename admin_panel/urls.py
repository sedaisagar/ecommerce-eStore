from django.urls import path

from admin_panel.views.common_views import AdminHomeView, AdminLoginView, AdminLogoutView
from admin_panel.views.users import AdminAdminListView, AdminUserListView

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='admin-login-page'),
    path('logout/', AdminLogoutView.as_view(), name='admin-logout-page'),

    # Authenticated Views
    path('', AdminHomeView.as_view(), name='admin-home-page'),
    
    path('users/admin/', AdminAdminListView.as_view(), name='admin-admin-list-page'),
    path('users/user/', AdminUserListView.as_view(), name='admin-user-list-page'),

    
]
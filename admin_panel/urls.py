from django.urls import path

from admin_panel.views import AdminHomeView, AdminLoginView

urlpatterns = [
    path('', AdminHomeView.as_view(), name='admin-home-page'),
    path('login/', AdminLoginView.as_view(), name='admin-login-page'),
]
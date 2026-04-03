from django.urls import path

from public_panel.views import HomePageView, AboutPageView, LoginPageView, RegisterPageView

urlpatterns = [
    path("login/",  LoginPageView.as_view(), name="login-page"),
    path("register/",  RegisterPageView.as_view(), name="register-page"),
    # 
    path("",  HomePageView.as_view(), name="home-page"),
    path("about/",  AboutPageView.as_view(), name="about-page"),
]
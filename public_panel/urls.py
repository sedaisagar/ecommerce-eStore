from django.urls import path

from public_panel.views import CategoryPageView, HomePageView, AboutPageView, LoginPageView, ProductDetailPageView, ProductListPageView, RegisterPageView, DashboardPageView

urlpatterns = [
    path("login/",  LoginPageView.as_view(), name="login-page"),
    path("register/",  RegisterPageView.as_view(), name="register-page"),
    path("dashboard/",  DashboardPageView.as_view(), name="dashboard-page"),
    # 
    path("",  HomePageView.as_view(), name="home-page"),
    path("about/",  AboutPageView.as_view(), name="about-page"),

    # Category and Product Pages
    path("categories/",  CategoryPageView.as_view(), name="category-page"),
    path("products/",  ProductListPageView.as_view(), name="product-page"),
    path("products/<str:pk>",  ProductDetailPageView.as_view(), name="product-detail-page"),
]
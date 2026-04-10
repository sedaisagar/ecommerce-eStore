from django.urls import include, path

from public_panel.views import (
    CartPageView, LoginPageView, LogoutView, RegisterPageView, 
    DashboardPageView,
    HomePageView, AboutPageView, 
    CategoryPageView, ProductDetailPageView, ProductListPageView,
    BlogDetailPageView, BlogListPageView, add_to_cart, 
    # APIs
    add_to_wishlist, 
)


urlpatterns = [
    path("login/",  LoginPageView.as_view(), name="login-page"),
    path('logout/', LogoutView.as_view(), name='logout-page'),
    # 
    path("register/",  RegisterPageView.as_view(), name="register-page"),
    path("dashboard/",  DashboardPageView.as_view(), name="dashboard-page"),
    # 
    path("",  HomePageView.as_view(), name="home-page"),
    path("about/",  AboutPageView.as_view(), name="about-page"),
    path("cart/",  CartPageView.as_view(), name="cart-page"),

    # Category and Product Pages
    path("categories/",  CategoryPageView.as_view(), name="category-page"),
    
    path("products/",  ProductListPageView.as_view(), name="product-page"),
    path("products/<str:pk>",  ProductDetailPageView.as_view(), name="product-detail-page"),
    # Blogs
    path("blogs/",  BlogListPageView.as_view(), name="blog-page"),
    path("blogs/<str:pk>",  BlogDetailPageView.as_view(), name="blog-detail-page"),

    # 

    path("api/", include(
        [
            path("add-to-wishlist/<str:product_id>/<str:action>", add_to_wishlist, name="add-to-wishlist"),
            path("add-to-cart/", add_to_cart, name="add-to-cart"),
        ]
    ))
]
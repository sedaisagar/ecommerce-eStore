from django.urls import path

from admin_panel.views.blogs import (
    BlogCategoryCreateView, BlogCategoryDeleteView, BlogCategoryEditView, BlogCategoryListView, 
    BlogTagCreateView, BlogTagDeleteView, BlogTagEditView, BlogTagListView,
    BlogCreateView, BlogDeleteView, BlogEditView, BlogListView,
)
from admin_panel.views.common_views import AdminHomeView, AdminLoginView, AdminLogoutView
from admin_panel.views.products import (
    ProductCategoryListView, ProductCategoryCreateView, ProductCategoryEditView, ProductCategoryDeleteView, 
    ProductTypeCreateView, ProductTypeDeleteView, ProductTypeEditView, ProductTypeListView, 
    ProductsCreateView, ProductsDeleteView, ProductsEditView, ProductsListView,
)
from admin_panel.views.users import AdminAdminListView, AdminUserListView

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='admin-login-page'),
    path('logout/', AdminLogoutView.as_view(), name='admin-logout-page'),

    # Authenticated Views
    path('', AdminHomeView.as_view(), name='admin-home-page'),
    
    path('users/admin/', AdminAdminListView.as_view(), name='admin-admin-list-page'),
    path('users/user/', AdminUserListView.as_view(), name='admin-user-list-page'),

    # Product Views

    path('products/categories/', ProductCategoryListView.as_view(), name='admin-product-cat-list'),
    path('products/categories/create/', ProductCategoryCreateView.as_view(), name='admin-product-cat-create'),
    path('products/categories/update/<str:pk>', ProductCategoryEditView.as_view(), name='admin-product-cat-edit'),
    path('products/categories/delete/<str:pk>', ProductCategoryDeleteView.as_view(), name='admin-product-cat-delete'),
   
    path('products/types/', ProductTypeListView.as_view(), name='admin-product-type-list'),
    path('products/types/create/', ProductTypeCreateView.as_view(), name='admin-product-type-create'),
    path('products/types/update/<str:pk>', ProductTypeEditView.as_view(), name='admin-product-type-edit'),
    path('products/types/delete/<str:pk>', ProductTypeDeleteView.as_view(), name='admin-product-type-delete'),

    path('products/', ProductsListView.as_view(), name='admin-product-list'),
    path('products/create/', ProductsCreateView.as_view(), name='admin-product-create'),
    path('products/update/<str:pk>', ProductsEditView.as_view(), name='admin-product-edit'),
    path('products/delete/<str:pk>', ProductsDeleteView.as_view(), name='admin-product-delete'),

    # Blog Views
    path('blogs/categories/', BlogCategoryListView.as_view(), name='admin-blog-cat-list'),
    path('blogs/categories/create/', BlogCategoryCreateView.as_view(), name='admin-blog-cat-create'),
    path('blogs/categories/update/<str:pk>', BlogCategoryEditView.as_view(), name='admin-blog-cat-edit'),
    path('blogs/categories/delete/<str:pk>', BlogCategoryDeleteView.as_view(), name='admin-blog-cat-delete'),
    
    path('blogs/tags/', BlogTagListView.as_view(), name='admin-blog-tag-list'),
    path('blogs/tags/create/', BlogTagCreateView.as_view(), name='admin-blog-tag-create'),
    path('blogs/tags/update/<str:pk>', BlogTagEditView.as_view(), name='admin-blog-tag-edit'),
    path('blogs/tags/delete/<str:pk>', BlogTagDeleteView.as_view(), name='admin-blog-tag-delete'),

    path('blogs/', BlogListView.as_view(), name='admin-blog-list'),
    path('blogs/create/', BlogCreateView.as_view(), name='admin-blog-create'),
    path('blogs/update/<str:pk>', BlogEditView.as_view(), name='admin-blog-edit'),
    path('blogs/delete/<str:pk>', BlogDeleteView.as_view(), name='admin-blog-delete'),

]
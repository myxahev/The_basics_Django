from django.urls import path

from admins.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, ProductUpdateView, \
    ProductListView, ProductDeleteView, ProductCreateView, ProductCategoryListView, ProductCategoryDeleteView, \
    ProductCategoryUpdateView, ProductCategoryCreateView, OrderListView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),

    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),

    path('products_create/', ProductCreateView.as_view(), name='products_create'),
    path('products/', ProductListView.as_view(), name='read_products'),
    path('products-update/<int:pk>/', ProductUpdateView.as_view(), name='products_update'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('category-products-create/', ProductCategoryCreateView.as_view(), name='category_products_create'),
    path('category-products/', ProductCategoryListView.as_view(), name='category_read_products'),
    path('category-products-update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='category_products_update'),
    path('category-product-delete/<int:pk>/', ProductCategoryDeleteView.as_view(), name='category_product_delete'),

    path('orders/', OrderListView.as_view(), name='read_orders'),

    # path('products_create/', products_create, name='products_create'),
    # path('products/', products_read, name='read_products'),
    # path('products-update/<int:id>/', products_update, name='products_update'),
    # path('product_delete/<int:id>/', product_delete, name='product_delete'),

]
from django.urls import path

from admins.views import index, admin_users_create, admin_users_update, admin_users_delete, admin_users, products_read, \
    products_update, products_create, product_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),

    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users/', admin_users, name='admin_users'),
    path('users-update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:id>/', admin_users_delete, name='admin_users_delete'),

    path('products_create/', products_create, name='products_create'),
    path('products/', products_read, name='read_products'),
    path('products-update/<int:id>/', products_update, name='products_update'),
    path('product_delete/<int:id>/', product_delete, name='product_delete'),

]
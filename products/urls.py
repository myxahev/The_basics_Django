from django.urls import path

from products.views import products
# from django.views.decorators.cache import cache_page

app_name = 'products'

urlpatterns = [
    path('', products, name='index'), # .../products/
    path('<int:category_id>/', products, name='category'), # ../products/<category_id>/
    path('page/<int:page>/', products, name='page'), # ../products/page/<page_num>/
    # path('category/<int:pk>', cache_page(3600)(products), name='category'),
    # path('product/<int:pk>', cache_page(3600)(product), name='detail'),
]
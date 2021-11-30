from django.shortcuts import render

from products.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import json
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import never_cache, cache_page


# module_dir = os.path.dirname(__file__)


# Create your views here.

def get_all_obj():
    if settings.LOW_CACHE:
        key = 'all_obj',
        all_obj = cache.get(key)
        if all_obj is None:
            all_obj = ProductCategory.objects.all()
            cache.set(key, all_obj)
        return all_obj
    else:
        return ProductCategory.objects.all()


def get_category(category_id):
    if settings.LOW_CACHE:
        key = f'category_{category_id}',
        category = cache.get(key)
        if category is None:
            category = Product.objects.filter(category_id=category_id)
            cache.set(key, category)
        return category
    else:
        return Product.objects.filter(category_id=category_id)


# def get_product(pk):
#     if settings.LOW_CACHE:
#         key = f'product_{pk}',
#         product = cache.get(key)
#         if product is None:
#             product = get_object_or_404(Product, pk=pk)
#             cache.set(key, product)
#         return product
#     else:
#         return get_object_or_404(Product, pk=pk)

# def get_products_order_by_price():
#     if settings.LOW_CACHE:
#         key = 'products',
#         products = cache.get(key)
#         if products is None:
#             products = Product.objects.filter(is_active=True, category__is_active=True, quantity__gte=1).order_by(
#                 'price')
#             cache.set(key, products)
#         return products
#     else:
#         return Product.objects.filter(is_active=True, category__is_active=True, quantity__gte=1).order_by('price')
#
#
# def get_products_in_category_orederd_by_price(pk):
#     if settings.LOW_CACHE:
#         key = f'products_in_category_orederd_by_price_{pk}'
#         products = cache.get(key)
#         if products is None:
#             products = Product.objects.filter(category__pk=pk, is_active=True,
#                                               category__is_active=True).order_by('price')
#             cache.set(key, products)
#         return products
#     else:
#         return Product.objects.filter(category__pk=pk, is_active=True,
#                                       category__is_active=True).order_by('price')

def get_products():
    if settings.LOW_CACHE:
        key = 'products',
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(quantity__gte=1).select_related(
                'category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(quantity__gte=1).select_related(
            'category')


def index(request):
    context = {'title': 'Geekshop'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'categories': get_all_obj()}
    if category_id:
        products = get_category(category_id)
    else:
        products = get_products()
    paginator = Paginator(products, 5)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)

    # file_path = os.path.join(module_dir, 'fixtures/products.json')
    # context['products'] = json.load(open(file_path, encoding='utf-8'))
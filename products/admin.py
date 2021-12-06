from django.contrib import admin
from products.models import Product, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', 'name', 'price', 'quantity', 'category', 'is_active')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category', 'is_active')
    readonly_fields = ('description',)
    ordering = ('name',)
    search_fields = ('name',)
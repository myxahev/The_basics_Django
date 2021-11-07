from .models import Product, ProductCategory
from django.forms import ModelForm, TextInput, FileInput, NumberInput


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price', 'quantity', 'category']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control py-4'
            }),
            'image': FileInput(attrs={
                'class': 'form-control py-4'
            }),
            'description': TextInput(attrs={
                'class': 'form-control py-4'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control py-4'
            }),
            'quantity': NumberInput(attrs={
                'class': 'form-control py-4'
            })
        }


class ProductCategoryUpdateForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control py-4'
            }),
            'description': TextInput(attrs={
                'class': 'form-control py-4'
            })
        }
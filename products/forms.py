from .models import Product
from django.forms import ModelForm, TextInput, FileInput, NumberInput, Select


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
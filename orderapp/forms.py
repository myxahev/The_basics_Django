from django import forms

from orderapp.models import Order

# class OrderForm(forms.ModelForm):
#     tagline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
#     about_me = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
#     gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
#
#     class Meta:
#         model = Order
#         exclude = ('user',)
#         fields = ('tagline', 'about_me', 'gender')
from products.models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label='цена', required=False)

    class Meta:
        model = Order
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['product'].queryset = Product.objects.filter(quantity__gte=1)
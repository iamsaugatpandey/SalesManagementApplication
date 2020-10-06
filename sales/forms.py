from django import forms

from .models import Customer, Product, Order, Delivery

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'email_address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'id': 'email_address'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sortno']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'sortno': forms.NumberInput(attrs={'class': 'form-control', 'id': 'sortno'})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product']

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control', 'id': 'customer'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
        }

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'order': forms.Select(attrs={'class': 'form-control', 'id': 'order'}),
            'courier_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'courier_name'}),
        }

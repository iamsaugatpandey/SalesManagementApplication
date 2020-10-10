from django import forms
from phone_field import PhoneField
from .models import Customer, Product, Order, Delivery, Vendor

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
        fields = ['name', 'quantity', 'vendor', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'id': 'quantity'}),
            'vendor': forms.Select(attrs={'class': 'form-control', 'id': 'vendor'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'id': 'color'}), 
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
            'pickup_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'pickup_name'}),

        }

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

        widgets = {
            'vendor_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'vendor_name'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'id': 'website'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
        }
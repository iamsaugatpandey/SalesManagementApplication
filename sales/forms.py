from django import forms

from .models import Customer, Product, Order, Delivery, Vendor

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'email', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'first_name',
            'data-val': 'true',
            'data-val-required': 'First name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'last_name',
                'data-val': 'true',
                'data-val-required': 'Last name',
            }),
            'address' : forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'data-val': 'true',
                'data-val-required': 'Please enter address',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'data-val': 'true',
                'data-val-required': 'Please enter email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'data-val': 'true',
                'min_length': 10,
                'max_length': 10,
                'data-val-required': 'Phone number without symbols',
            })
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
        fields = ['customer', 'product', 'quantity']

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control', 'id': 'customer'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'id': 'quantity'})
        }

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        exclude = ['order', 'created_date']

        widgets = {
            'courier_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'courier_name'}),
            'pickup_in_person': forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'pickup_in_person'}),
            'pickup_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'pickup_name'})
        }

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'phone', 'website']

        widgets = {
            'vendor_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'vendor_name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'id': 'website'})
        }


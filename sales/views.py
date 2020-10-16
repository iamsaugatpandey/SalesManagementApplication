from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


from users.models import User
from .models import (
    Customer,
    Product,
    Order,
    Delivery,
    Vendor
)

from .forms import (
    CustomerForm,
    ProductForm,
    OrderForm,
    DeliveryForm,
    VendorForm
)

# THIS IS FOR CUSTOMER VIEW
@login_required(login_url='login')
def create_customer(request):
    forms = CustomerForm()
    if request.method == 'POST':
        forms = CustomerForm(request.POST)
        if forms.is_valid():
            first_name = forms.cleaned_data['first_name']
            last_name = forms.cleaned_data['last_name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            phone = forms.cleaned_data['phone']
            
            Customer.objects.create(
                first_name=first_name, 
                last_name=last_name, 
                address=address, 
                email=email, 
                phone=phone
                )
            return redirect('/sales/customer-list')
    context = {
        'form': forms
    }
    return render(request, 'customer/create_customer.html', context)

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customer_list'

# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/sales/product-list')
    context = {
        'form': forms
    }
    return render(request, 'product/create_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'product_list'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            customer = forms.cleaned_data['customer']
            product = forms.cleaned_data['product']
            quantity = forms.cleaned_data['quantity']
            Order.objects.create(
                customer=customer,
                product=product,
                quantity = quantity,
                status='pending'
            )
            return redirect('/sales/order-list')
    context = {
        'form': forms
    }
    return render(request, 'order/create_order.html', context)

def order_list(request):
    if request.method == 'GET':
        order_list = Order.objects.all().order_by('id')
        context = {'order_list': order_list}
    return render(request, 'order/order_list.html', context)

def order_detail(request, order_id):
    if request.method == 'GET':
        order = Order.objects.get(id=order_id)
        customer = Customer.objects.get(id=order.customer.id)
        if Delivery.objects.filter(order=order_id):
            delivery = Delivery.objects.get(order=order_id)
            context = {
                'order': order,
                'customer': customer,
                'delivery': delivery
            }
            return render(request, 'order/order_detail.html', context)
        else:
            context = {
                'order': order,
                'customer': customer,
            }
            return render(request, 'order/order_detail.html', context)

# Delivery views
@login_required(login_url='login')
def create_delivery(request, order_id):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            delivery = forms.save(commit=False)
            delivery.order = Order.objects.get(id=order_id)
            delivery.save()
            return redirect('/sales/delivery-list')
    order = Order.objects.get(id=order_id)
    context = {
        'order': order,
        'form': forms,
    }
    return render(request, 'delivery/create_delivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'delivery/delivery_list.html'
    context_object_name = 'delivery_list'

# Vendor views
@login_required(login_url='login')
def create_vendor(request):
    forms = VendorForm()
    if request.method == 'POST':
        forms = VendorForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/sales/vendor-list')
    context = {
        'form': forms
    }
    return render(request, 'vendor/create_vendor.html', context)


class VendorListView(ListView):
    model = Vendor
    template_name = 'vendor/vendor_list.html'
    context_object_name = 'vendor_list'
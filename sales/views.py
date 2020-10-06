from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
# Create your views here.


from users.models import User
from .models import (
    Customer,
    Product,
    Order,
    Delivery
)

from .forms import (
    CustomerForm,
    ProductForm,
    OrderForm,
    DeliveryForm
)

# THIS IS FOR CUSTOMER VIEW
@login_required(login_url='login')
def create_customer(request):
    forms = CustomerForm()
    if request.method == 'POST':
        forms = CustomerForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('customer-list')
    context = {
        'form': forms
    }
    return render(request, 'sales/create_customer.html', context)

class CustomerListView(ListView):
    model = Customer
    template_name = 'sales/customer_list.html'
    context_object_name = 'customer'

# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'sales/create_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'sales/product_list.html'
    context_object_name = 'product'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            customer = forms.cleaned_data['customer']
            product = forms.cleaned_data['product']
            Order.objects.create(
                customer=customer,
                product=product,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'sales/create_order.html', context)

class OrderListView(ListView):
    model = Order
    template_name = 'sales/order_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context

# Delivery views
@login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'sales/create_delivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'sales/delivery_list.html'
    context_object_name = 'delivery'


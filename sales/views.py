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
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            first_name = forms.cleaned_data['first_name']
            last_name = forms.cleaned_data['last_name']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, password=password, email=email, is_customer=True)
                Customer.objects.create(user=user, name=name, address=address)
                return redirect('customer-list')
    context = {
        'form': forms
    }
    return render(request, 'customer/create_customer.html', context)

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customer'

# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProsuctForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'product/create_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
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
            quantity = forms.cleaned_data['quantity']
            first_name = forms.cleaned_data['first_name']
            last_name = forms.cleaned_data['last_name']
            email = forms.cleaned_data['email']
            Order.objects.create(
                customer=customer,
                product=product,
                quantity=quantity,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'order/create_order.html', context)

def order_list(request):
    if request.method == 'GET':
        search = request.GET.get('site_search', 'null')
        if True: #if search == 'null' 
            order_list = Order.objects.all().order_by('id')
        else:
            product_id = Product.objects.filter(name__contains=str(search))
            order_list = Order.objects.filter(product=product_id)
        context = {'order_list': order_list}
    return render(request, 'order/order_list.html', context)
    # model = Order
    # template_name = 'order/order_list.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['order'] = Order.objects.all().order_by('-id')
    #     return context

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
    return render(request, 'store/create_delivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'


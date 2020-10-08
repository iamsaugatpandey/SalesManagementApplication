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
    context = {}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Customer.objects.create(first_name=first_name, last_name=last_name, address=address, email=email, phone=phone)
        return redirect('/sales/customer-list')

        # except ObjectDoesNotExist:
        #     context = {
        #         'message': "No matching records for email."
        #     }
        #     return render(request, 'order/create_order.html', context)
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
    context = {}
    if request.method == 'POST':
        try:
            customer = Customer.objects.get(email__iexact=request.POST.get('email'))
            product = Product.objects.get(name__iexact=request.POST.get('product'))
            quantity = request.POST.get('quantity')
            Order.objects.create(
                customer=customer,
                product=product,
                quantity=quantity,
                status='pending'
            )
            return redirect('/sales/order-list')
        except ObjectDoesNotExist:
            context = {
                'message': "No matching records for email."
            }
            return render(request, 'order/create_order.html', context)
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


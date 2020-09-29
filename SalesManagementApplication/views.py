from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from sales.models import Product, Customer, Order

@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_order = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    context = {
        'product': total_product,
        'customer': total_customer,
        'order': total_order,
        'orders': orders
    }
    return render(request, 'dashboard.html', context)
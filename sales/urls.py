from django.urls import path


from .views import (
    create_customer,
    create_product,
    create_order,
    create_delivery,

    CustomerListView,
    ProductListView,
    order_list,
    DeliveryListView,
)

app_name = 'sales'
urlpatterns = [
    path('create-customer/', create_customer, name='create-customer'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('customer-list/', CustomerListView.as_view(), name='customer-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', order_list, name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
]
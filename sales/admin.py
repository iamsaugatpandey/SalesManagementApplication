from django.contrib import admin

# Register your models here.

from .models import (
    Customer, 
    Product, 
    Order, 
    Delivery,
    Vendor
)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'address', 'created_date']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Vendor)
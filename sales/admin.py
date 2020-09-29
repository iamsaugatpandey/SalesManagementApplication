from django.contrib import admin

# Register your models here.

from .models import (
    Customer, 
    Product, 
    Order, 
    Delivery
)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
from django.db import models
from users.models import User
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=120, unique=True, default='Name')
    address = models.CharField(max_length=220)
    email_address = models.CharField(max_length=100, default='SOME STRING')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    quantity = models.PositiveIntegerField()
    color = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('complete', 'Complete'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    pickup_name = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.vendor_name

from django.db import models
from users.models import User
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=120, default='Joe')
    last_name = models.CharField(max_length=120, default='Doe')
    email = models.CharField(max_length=120, default='jdoe@fashion.com', unique=True)
    address = models.CharField(max_length=220)
    phone = models.CharField(max_length=10)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    quantity = models.PositiveIntegerField()
    product_type = models.ForeignKey('Type', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Type(models.Model):
    type_name = models.CharField(max_length=50, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.type_name

class Color(models.Model):
    color_name = models.CharField(max_length=50, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.color_name

class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('complete', 'Complete'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pickup_in_person = models.BooleanField(default=True)
    courier_name = models.CharField(max_length=120)
    pickup_name = models.CharField(max_length=100, default='Mary Howl')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    website = models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.vendor_name
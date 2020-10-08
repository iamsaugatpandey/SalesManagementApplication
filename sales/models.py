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
        return self.first_name + self.last_name

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

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
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name
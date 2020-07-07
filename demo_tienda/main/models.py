from django.db import models
from enum import Enum

# Table Users
class Users (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)

# Table Phones
class Phones (models.Model):
    number = models.CharField(max_length=9)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)

# Table States
class States (models.Model):
    name = models.CharField(max_length=50)

# Table Cities
class Cities (models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(States, on_delete=models.CASCADE, null=False)

# Table Adresses
class Adresses (models.Model):
    full_adress = models.CharField(max_length=250)
    main = models.BooleanField(default=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)

# Enum for product status
class Product_Status (Enum):
    OUT_OF_STOCK = "Out of Stock"
    IN_STOCK = "In Stock"
    RUNNING_LOW = "Running low" # Less than 20

# Table Products
class Products (models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

# Enum for order status
class Order_Status (Enum):
    ORDERED = 'Ordered'
    PAID_OUT = 'Paid out'
    PREPARED = 'Prepared'
    SENT = 'Sent'
    DELIVERED = 'Delivered'

# Table Orders
class Orders (models.Model):
    date = models.DateField()
    status = models.CharField(
        max_length = 5,
        choices = [(tag, tag.value) for tag in Order_Status]
    )
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)

class Order_Items (models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField()
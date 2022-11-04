from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_img = models.ImageField(upload_to='static/img')


class Cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    
class Order(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)
    total = models.FloatField(max_length=100)


class Order_Items(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()    
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
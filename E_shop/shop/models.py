from email.policy import default
from turtle import back
from unicodedata import category
from venv import create
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=150,null=True, blank=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='shop/category/', default='shop/category/noImageCategory.png' )
    def __str__(self):
        return self.name
class Tag (models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class ColorProduct(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class StatusProduct(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=150)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    material = models.CharField(max_length=150,null=True, blank=True)
    price = models.CharField(max_length=150)
    image_front = models.ImageField(upload_to='shop/'+'/front/', default='shop/noImageProduct.png' )
    image_back = models.ImageField(upload_to='shop/'+'/back/', default='shop/noImageProduct.png')
    description = models.TextField(default = "This product is not description")
    discout = models.FloatField(default=1)
    create_date= models.DateTimeField(default=timezone.now)
    user_update_last = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    tag = models.ManyToManyField(Tag, null=True, blank =True)
    color = models.ForeignKey(ColorProduct, on_delete=models.SET_NULL,null=True)
    status_product =  models.ForeignKey(StatusProduct, on_delete=models.SET_NULL,default=1, null=True)
    def __str__(self):
        return self.name
        
class Thumnails(models.Model):
    name = models.CharField(max_length=150)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='shop/', default='shop/noImageProduct.png')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class SizeProduct(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name   


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ManyToManyField(SizeProduct, null=True, blank =True)
    quantity = models.ImageField(default = 0)
    def __str__(self):
        return self.name       
    

    

    



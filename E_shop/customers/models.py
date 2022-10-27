from django.db import models
from django.utils import timezone
# Create your models here.

class Customer_role(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

# Create your models here.
class Customer(models.Model):
    Customer_role = models.ForeignKey(Customer_role, on_delete=models.PROTECT,default=1)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=400,null=True,blank=True)
    image = models.ImageField(upload_to='users/customers', default='users/customers/noavatar.png')
    create_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.fullname


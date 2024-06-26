from django.db import models
from django.contrib.auth.models import User
#from django.utils.timezone

# Create your models here.
class Users(models.Model):
    Username=models.CharField(max_length=255,primary_key=True,unique=True)
    Fullname=models.CharField(max_length=255)
    Email=models.CharField(max_length=255,unique=True)
    Password=models.CharField(max_length=255,unique=True)
    Phone_number=models.IntegerField(unique=True)

class Product(models.Model):
    ID=models.IntegerField(primary_key=True,unique=True)
    Name=models.CharField(max_length=255,unique=True)
    Suger=models.IntegerField()
    Coffe=models.IntegerField()
    Flour=models.IntegerField()
    Chocolate=models.IntegerField()
    Vertical=models.BinaryField()
    Price=models.IntegerField()
    Sales=models.IntegerField(default=0)
    #Image=models.ImageField(upload_to='product_images/')
class Orders(models.Model):
    Order_ID=models.IntegerField(primary_key=True,unique=True)
    Username=models.CharField(max_length=255)
    Products=models.CharField(max_length=255)
    Purchase_amount=models.IntegerField()
    Type=models.BinaryField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    #date=models.DateField(default=datetime.datetime.today())

class Admins(models.Model):
    Username=models.CharField(max_length=255,primary_key=True,unique=True)
    Email=models.CharField(max_length=255,unique=True)
    Password=models.CharField(max_length=255,unique=True)
class Storage(models.Model):
    ID=models.IntegerField(primary_key=True,unique=True)
    Name=models.CharField(max_length=255,unique=True)
    Amount=models.IntegerField()

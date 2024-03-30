from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=50, null=True)

class seller(models.Model):
    name = models.TextField(max_length=50, null=True) 
    email= models.TextField(max_length=100,null=True)
    password= models.TextField(max_length=100,null=True)
class Product(models.Model):
    name = models.TextField(max_length=50, null=True)
    price = models.FloatField(null=True)
    description = models.TextField(max_length=100, null=True)
    image = models.ImageField(upload_to='photos', null=True)
    category=models.ForeignKey(Category,on_delete= models.CASCADE,null=True)


    

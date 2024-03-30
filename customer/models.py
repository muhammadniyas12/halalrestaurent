from django.db import models
from seller.models import*

# Create your models here.


class customer(models.Model):
    name = models.TextField(max_length=50, null=True)
    email = models.TextField(max_length=100, null=True)
    pswd1= models.TextField(max_length=100, null =True)



class Cart(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)


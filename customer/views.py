from django.shortcuts import render,redirect
from.models import*
from seller.models import *
from django.shortcuts import render, HttpResponseRedirect, Http404, get_object_or_404
from django.http import HttpResponse
# Create your views here.
def signup(request):
    if request.method =='POST':
         name=request.POST['name']
         email=request.POST['email']
         password=request.POST['password']
         cust=customer(name=name,email=email,pswd1=password)
         cust.save()
         return redirect('customer:cust_login')
    return render(request,'customer/signup.html')
def aboutus(request):
     return render(request,'customer/aboutus.html')
def contact(request):
     return render(request,'customer/contact.html')
def home(request):
     return render(request,'customer/home.html')


   
def  cart(request):
     cart_items=Cart.objects.all()
     total_price=sum(item.product.price*item.quantity for item in cart_items)
     total_price_per_item=[]
     grand_total=0
     for item in cart_items:
          item_total=item.product.price*item.quantity
          total_price_per_item.append({'item':item,'total':'item_total'})
          grand_total+=item_total
     return render(request,'customer/cart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})

def   payment(request):
     return render(request,'customer/payment.html')
 
def  viewpdt(request):
     pdt=Product.objects.all()
     return  render(request,'customer/viewpdt.html',{'products':pdt})
def cust_login(request):
     if request.method =='POST':

        
         email=request.POST['email']
         password=request.POST['password']

         if customer.objects.filter(email=email,pswd1=password).exists():
              return redirect('customer:viewpdt')
         else:
              return render(request,'customer/cust_login.html',{'msg':'invalid detail '})
     
     return render(request,'customer/cust_login.html')



def add_to_cart(request,product_id):
     
     if request.method=='POST':
          
          product=Product.objects.get(id=product_id)
          

          cart_item,created=Cart.objects.get_or_create(product=product)
          if not created:
               cart_item.quantity+=1
               cart_item.save()
          return redirect('customer:cart')      




    


def remove_from_cart(request,product_id):
     product=Product.objects.get(id=product_id)
     cart_item=cart.objects.get(product=product)
     cart_item.delete()
     return redirect('customer:cart')
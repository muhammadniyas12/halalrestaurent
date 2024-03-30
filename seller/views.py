from django.shortcuts import render,redirect
from .models import *

def home(request):
    return render(request,'seller/home.html')
def viewpdt(request):
    pdt= Product.objects.all()
    return render(request,'seller/viewpdt.html',{'products':pdt})
def dashboard(request):
    return render(request,'seller/dashboard.html')
def slogin(request):
     if request.method =='POST':

        
         email=request.POST['email']
         password=request.POST['password']

         if seller.objects.filter(email=email,password=password).exists():
              return redirect('seller:viewpdt')
         else:
              return render(request,'seller/slogin.html',{'msg':'invalid detail '})
     return  render(request,'seller/slogin.html')
def  update(request):
    return   render(request,'seller/update.html')
def  deletepdt(request,pid):
    Product.objects.get(id=pid).delete()
    return  redirect('seller:viewpdt')
def updatepdt(request,pid):
    categorys=Category.objects.all()
    pdt=Product.objects.get(id=pid)
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        description=request.POST['description']
        image=request.FILES['image']
        cate=request.POST['category']
        category=Category.objects.get(id=cate)

        pdt.name=name
        pdt.price=price
        pdt.description=description
        pdt.category=category
        pdt.image=image

        pdt.save()
        return redirect('seller:viewpdt')
    return render(request,'seller/update.html',{'categorys':categorys,'pdt':pdt})

    

    
    





def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        pswd1=request.POST['pswd1']
        pswd2=request.POST['pswd2']
        sel=seller(name=name,email=email,password=pswd1 )
        sel.save()
        
        return    redirect('seller:login')
    
    return render(request,'seller/signup.html')





def adpdt(request):
    categorys=Category.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        description=request.POST['description']
        cate=request.POST['category']
        image=request.FILES['image']
        category=Category.objects.get(id=cate)
        sel=Product(name=name,price=price,description=description,category=category,image=image)
        sel.save()

        return redirect('seller:viewpdt')
    

    return render(request,'seller/adpdt.html',{'categorys':categorys})


  



    

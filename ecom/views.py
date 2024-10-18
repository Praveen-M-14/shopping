from http.client import HTTPResponse
from django.shortcuts import redirect, render
from ecom.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    products=Product.objects.filter(trending = 1)
    return render(request,"ecom/index.html",{"products":products})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
        return redirect("/login")



def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
     if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return("/")
        else:
            messages.error(request,"Invalid User Name or password")
            return redirect("/login")
    return render(request,"ecom/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now")
            return redirect('/login')
    return render(request,"ecom/register.html",{'form':form})

#def collections(request):
 #   Catagory=catagory.objects.filter(status=0)
  #  return render(request,"ecom/collections.html",{"Catagory":Catagory})
def collections(request):
    catagory = Catagory.objects.all()  # Fetch categories from database
    return render(request, 'ecom/collections.html', {'Categories': catagory})

def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
       products=Product.objects.filter(catagory__name=name) # Fetch categories from database
       return render(request, 'ecom/products/index.html', {'products': products,"catagory_name":name})
    else:
        messages.warning(request,"NO Such product Found")


def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"ecom/products/productdetails.html",{"products":products})
        else:
            messages.error(request,"No Such product Found")
            return redirect('collections')
    else:
       messages.error(request,"No Such Catagory Found")
       return redirect('collections')
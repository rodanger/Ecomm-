
from collections import UserDict, UserList
from curses import use_default_colors
from operator import truediv
import re
from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth import authenticate,login 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='Login')
def index(request):
    x = Products.objects.all()
    return render(request,'home/index.html',{'pro':x})


def product_detail(request,id):
    x = Products.objects.get(id=id)
    return render(request,'home/product-detail.html',{'pro':x})


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return index(request)
        else:
            msg = "Invalid Credentials"
            return render(request,'home/login.html',{'m':msg})
        
    return render(request,'home/login.html')


def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 == pass2:
            user = UserList.objects.filter(username=username).exists()
            if user == False:
                usr = UserDict(username=username,password=pass1)
                usr.save()
                return redirect('Login')
            else:
                msg = "Username already exists!"
                return render(request,'home/signup.html',{'m':msg})    

        else:
            msg = "Password not matching"
            return render(request,'home/ signup.html',{'m':msg})



    return render(request,'home/signup.html')


def cart(request):
    usr_id = request.user.id
    x = Cart.objects.filter(user_id = usr_id) 

    if x.count() <= 0 and request.method != 'POST':
        msg = "No Items in cart"
        return render(request,'home/cart.html',{'m':msg})


    if request.method == 'POST':
        print("POST METHOD")
        product = request.POST.get('product')
        qnty = request.POST.get('qnty')
        if int(qnty) > 0:
            usr_id = request.user.id
            pro = Products.objects.get(id=product)
            tot = int(qnty) * pro.product_price
            x1 = Cart(user_id = usr_id,product_id=pro,quantity=qnty,total_price=tot)
            x1.save()
            return render(request,'home/cart.html',{'items':x})

    return render(request,'home/cart.html',{'items':x})

           

def save_order(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        num = request.POST.get('num')
        add1 = request.POST.get('add1')
        add2 = request.POST.get('add2')
        pin = request.POST.get('pin')

        usr_id = request.user.id 

        # Calculate total Price       

        x = Cart.objects.filter(user_id = usr_id)
        total_price = 0
        for i in x:
            total_price += i.total_price
           

        # Save to Database

        order = Order(user_id=usr_id,name=name,phone=num,add1=add1,add2=add2,pin=pin,total=total_price)    
        order.save()
        

        # Save to Order Items
        for i in x:
            o1 = Order_Items(user_id=usr_id,order_id= order.id,product_id=i.product_id,quantity=i.quantity,total_price=i.total_price)
            o1.save()
            i.delete()

        
        #Redirect to home page
        prods = Products.objects.all()
        msg ="Order Placed Successfully"
        return render(request,'home/index.html',{'pro':prods,'m':msg})
        
    return index(request)

    
def myorders(request):
    usr_id = request.user.id
    x = Order_Items.objects.filter(user_id = usr_id)
    return render(request,'home/myorders.html',{'itms':x})


def remove(request,id):
    x = Cart.objects.get(id=id)
    x.delete()
    return redirect('cart')

















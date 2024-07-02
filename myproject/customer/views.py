from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth

import logging

from customer.models import Addr,Cartinfo,Buyinfo, Orderdetails
# Create your views here.

def login(request):
    if request.method == 'POST':
        un=request.POST.get('username')
        pass1= request.POST.get('password')
        User=auth.authenticate(username=un,password=pass1)
        if User is not None:
            auth.login(request,User)
            return redirect('home')
        else:
            messages.error(request,"username and password not valid please  conform are you registered or not")
            return redirect('login')

    return render(request,'customer/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def bestseller(request):
    return render(request,'customer/bestseller.html')



logger = logging.getLogger(__name__)

@login_required(login_url='login')
def address(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        pincode = request.POST.get('pincode')
        housename = request.POST.get('housename')
        area = request.POST.get('area')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        state = request.POST.get('state')
        data = Addr(user=request.user,country=country,name=name,mobile=mobile,pincode=pincode,housename=housename,area=area,landmark=landmark,city=city,state=state)
        data.save()
        return redirect('home')
    
    return render(request,'customer/address.html')

def registration(request):
    if request.method =='POST':
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        un = request.POST.get('un')
        em = request.POST.get('em')
        pass1 =request.POST.get('pass')
        cpass1 =request.POST.get('cpass')
        if pass1==cpass1:
            if User.objects.filter(username=un).exists():
                messages.error(request,'user alraeady exists use another')
                return redirect('registration')
            else:
                if User.objects.filter(email=em).exists():
                    messages.error(request,'emaillaready exists use another')
                    return redirect('registration')
                else:
                    User.objects.create_user(first_name=fn,last_name=ln,username=un,email=em,password=pass1)
                    return redirect('login')

        else:
            messages.error(request,'password not matched enter correct')
            return redirect('registration')
            
    return render(request,'customer/registration.html')




def cartview(request):
    if request.method == 'POST':
        cartimage = request.POST.get('cartimage')
        cartinfo = request.POST.get('cartinfo')
        cartprice = request.POST.get('cartprice')
        quantity = int(request.POST.get('quantity', 1))
        data=Cartinfo(user=request.user,cartimage=cartimage,cartinfo=cartinfo,cartprice=cartprice,quantity=quantity)
        data.save()
        return redirect('home')
    




def buyview(request):
    if request.method == 'POST':
        buyimage = request.POST.get('buyimage')
        buyinfo = request.POST.get('buyinfo')
        buyprice = request.POST.get('buyprice')
        data=Buyinfo(user=request.user,buyimage=buyimage,buyinfo=buyinfo,buyprice=buyprice)
        data.save()
        return redirect('home')



@login_required(login_url='login')
def chekout(request):
    if request.method == 'POST':
        cartitems = Cartinfo.objects.filter(user=request.user)
        
        if not cartitems.exists():
        
            messages.error(request, 'Your cart is empty.')
            return redirect('chekout')
        total_amount = sum(item.cartprice * item.quantity for item in cartitems)
        # Move Cartinfo items to Buyinfo
        for item in cartitems:
            Buyinfo.objects.create(
                user=request.user,
                buyimage=item.cartimage,
                buyinfo=item.cartinfo,
                buyprice=item.cartprice
            )

        # Clear the cart after processing
        cartitems.delete()

        l=Orderdetails.objects.all()
        nl=[]
        for i in l:
            nl.append(i.id)
        
            
        productid=nl[-1]

        return redirect('ordersummary',productidorderdetail=productid)
    
    cartitems = Cartinfo.objects.filter(user=request.user)
    quantity = sum(item.quantity for item in cartitems)
    total_amount = sum(item.cartprice * item.quantity for item in cartitems)
    totalwithgst = sum(item.totalwithgst for item in cartitems)
    totalwithoutgst = sum(item.total_price for item in cartitems)
    # totalprice=self.total_price

    customer= Addr.objects.filter(user=request.user)
    
    context = {
        'quantity':quantity,
        'cart_items': cartitems,
        'total_amount': total_amount,
        'totalwithgst': totalwithgst,
        'totalwithoutgst': totalwithoutgst,
        'customer':customer,
    }
    return render(request, 'customer/chekout.html', context)




@login_required(login_url='login')
def ordersummary(request,productidorderdetail):
    product = Buyinfo.objects.filter(user=request.user)
    
    # return render(request, 'product_summary.html', context)

    buy_items = Buyinfo.objects.filter(user=request.user)

    cartitems = Cartinfo.objects.filter(user=request.user)
    quantity = sum(item.quantity for item in cartitems)
    total_amount = sum(item.cartprice * item.quantity for item in cartitems)
    total_amount_with_gst = sum(item.totalwithgst for item in cartitems)
    total_amount_excluding_gst = sum(item.total_price for item in cartitems)
    
    orderdata = Orderdetails.objects.filter(user=request.user,id=productidorderdetail)
    context = {
        'product': product,
        'quantity':quantity,
        'cartitems': cartitems,
        'total_amount': total_amount,
        'total_amount_with_gst': total_amount_with_gst,
        'total_amount_excluding_gst': total_amount_excluding_gst,
        'buy_items': buy_items,
        'orderdata':orderdata,
    }

    return render(request, 'customer/ordersummary.html',context)


def orderdetails(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        caddress = request.POST.get('caddress')
        cpincode = request.POST.get('cpincode')
        cmobile = request.POST.get('cmobile')
        cquantity = request.POST.get('cquantity')
        ctotalwithoutgst = request.POST.get('ctotalwithoutgst')
        ctotalwithgst = request.POST.get('ctotalwithgst')
        data=Orderdetails(user=request.user,cname=cname,caddress=caddress,cpincode=cpincode,cmobile=cmobile,cquantity=cquantity,ctotalwithoutgst=ctotalwithoutgst,ctotalwithgst=ctotalwithgst)
        data.save()
        return redirect('chekout')



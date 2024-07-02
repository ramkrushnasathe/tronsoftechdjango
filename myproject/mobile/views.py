from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from customer.models import Cartinfo,Buyinfo
from django.contrib import messages
# from customer.models import cart,Buy

# Create your views here.

def mobile1(request):
    return render(request,'mobile/mobile1.html')
def mobile2(request):
    return render(request,'mobile/mobile2.html')
def mobile3(request):
    return render(request,'mobile/mobile3.html')
def mobile4(request):
    return render(request,'mobile/mobile4.html')


@login_required(login_url='login')
def cartdata(request):
    cartdata = Cartinfo.objects.filter(user=request.user)
    # cartitems = Cartinfo.objects.filter(user=request.user)
    total_amount = sum(item.cartprice * item.quantity for item in cartdata)
    total_amount_with_gst = sum(item.totalwithgst for item in cartdata)
    total_amount_excluding_gst = sum(item.total_price for item in cartdata)
    quantity = sum(item.quantity for item in cartdata)
    context = {
        'quantity':quantity,
        'cartdata': cartdata,
        'total_amount_with_gst':total_amount_with_gst,
        'total_amount_without_gst':total_amount_excluding_gst,
    }
    return render(request, 'customer/cart.html', context)




@login_required(login_url='login')
def buydata(request):
    buydata=Buyinfo.objects.filter(user=request.user)
    context={
        'buydata':buydata,
        
    }
    return render(request,'customer/buydata.html',context)


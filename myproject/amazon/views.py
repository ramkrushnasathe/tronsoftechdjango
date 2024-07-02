from django.shortcuts import render

def home(request):
    return render(request,'amazon/home.html')

def sell(request):
    return render(request,'amazon/sell.html')

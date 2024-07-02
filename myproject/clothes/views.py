from django.shortcuts import render

# Create your views here.

def clothes1(request):
    return render(request,'clothes/clothes1.html')

def clothes2(request):
    return render(request,'clothes/clothes2.html')

def clothes3(request):
    return render(request,'clothes/clothes3.html')

def clothes4(request):
    return render(request,'clothes/clothes4.html')
from django.shortcuts import render


# Create your views here.

def beauty1(request):
    return render(request,'beauty/beauty1.html')

def beauty2(request):
    return render(request,'beauty/beauty2.html')

def beauty3(request):
    return render(request,'beauty/beauty3.html')

def beauty4(request):
    return render(request,'beauty/beauty4.html')
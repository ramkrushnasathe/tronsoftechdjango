from django.contrib import admin
from django.urls import path
from customer.views import *

urlpatterns = [
    path('login/',login,name='login'),
    path('bestseller/',bestseller,name='bestseller'),
    path('address/',address,name='address'),
    path('registration/',registration,name='registration'),
    path('cartview/',cartview,name='cartview'),
    path('buyview/',buyview,name='buyview'),
    path('orderdetails/',orderdetails,name='orderdetails'),
    path('chekout/',chekout,name='chekout'),
    path('ordersummary/<int:productidorderdetail>/',ordersummary,name='ordersummary'),
    path('logout/',logout,name='logout')
    
    
    
]
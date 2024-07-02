from django.contrib import admin
from django.urls import path
from amazon.views import *

urlpatterns = [
    path('',home,name='home'),
    path('sell/',sell,name='sell')
]
from django.contrib import admin
from django.urls import path
from clothes.views import *

urlpatterns = [
    path('clothes1/',clothes1,name='clothes1'),
    path('clothes2/',clothes2,name='clothes2'),
    path('clothes3/',clothes3,name='clothes3'),
    path('clothes4/',clothes4,name='clothes4'),
]
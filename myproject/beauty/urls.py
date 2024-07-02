from django.contrib import admin
from django.urls import path
from beauty.views import *

urlpatterns = [
    path('beauty1/',beauty1,name='beauty1'),
    path('beauty2/',beauty2,name='beauty2'),
    path('beauty3/',beauty3,name='beauty3'),
    path('beauty4/',beauty4,name='beauty4'),
]
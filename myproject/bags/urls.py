from django.contrib import admin
from django.urls import path
from bags.views import *

urlpatterns = [
    path('bags1/',bags1,name='bags1'),
    path('bags2/',bags2,name='bags2'),
    path('bags3/',bags3,name='bags3'),
    path('bags4/',bags4,name='bags4'),
]
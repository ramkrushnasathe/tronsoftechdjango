from django.contrib import admin
from customer.models import *
# Register your models here.

class AddrAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Addr,AddrAdmin)
admin.site.register(Cartinfo)
admin.site.register(Buyinfo)
admin.site.register(Orderdetails)
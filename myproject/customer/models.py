from decimal import ROUND_HALF_UP, Decimal
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Addr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    mobile=models.BigIntegerField()
    pincode=models.IntegerField()
    housename=models.CharField(max_length=255)
    area=models.CharField(max_length=255)
    landmark=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username}\'s Address'
    
class Cartinfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cartimage = models.CharField(max_length=255)
    cartinfo = models.CharField(max_length=255)
    cartprice = models.DecimalField(max_digits=10, decimal_places=2)
    quantity  = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.cartinfo
    


    @property
    def total_price(self):
        return self.cartprice * self.quantity

    @property
    def gst_amount(self):
        # Assuming GST rate is 18%
        gst_rate = Decimal('0.18')
        return (self.total_price * gst_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    @property
    def totalwithgst(self):
        return self.total_price + self.gst_amount

    


class Buyinfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    buyimage = models.CharField(max_length=255)
    buyinfo = models.CharField(max_length=255)
    buyprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.buyinfo
    
class Orderdetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    cname=models.CharField(max_length=255)
    caddress=models.CharField(max_length=255)
    cpincode=models.CharField(max_length=255)
    cmobile=models.CharField(max_length=255)
    cquantity=models.CharField(max_length=255)
    ctotalwithoutgst=models.CharField(max_length=255)
    ctotalwithgst=models.CharField(max_length=255)

    def __str__(self):
        return self.cname



    
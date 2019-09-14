from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfil(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    mobile =models.CharField(max_length=10)

class Item(models.Model):
    typ= models.CharField(max_length=30)
    phonenum=models.CharField(max_length=10)
    price=models.CharField(max_length=7)
    x={
        ('R','Riyadh'),
        ('J','Jeddah'),
        ('D','Dammam')
    }
    city=models.CharField(max_length=1,choices=x)
    Manufacturer=models.CharField(max_length=30)
    start_on=models.DateTimeField(default=timezone.now)
    picture =models.ImageField(upload_to='items')

    def __str__(self):
        return self.typ

   


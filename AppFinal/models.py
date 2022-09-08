from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length= 40)
    price = models.FloatField()
    desc = models.TextField()
    SKU = models.CharField(max_length=30)
    stock = models.BooleanField(default= True)
    image = models.ImageField(upload_to='producto_image', default='producto_image/descarga.png')
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)
   
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length= 40, default= "client")
    email = models.EmailField()
    first_name =  models.CharField(max_length= 40)
    last_name =  models.CharField(max_length= 40)

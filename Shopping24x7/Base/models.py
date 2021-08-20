# django imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# local imports
from constants import *

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=300, unique=True)
    USERNAME_FIELD ='email'
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.FileField(upload_to='productimg/', null=True, verbose_name="")

    def __str__(self):
        return str(self.id)


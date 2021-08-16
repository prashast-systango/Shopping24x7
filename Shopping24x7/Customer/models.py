from django.db import models
from django.contrib.auth.models import User
from constants import *




class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=300)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50, choices=STATE_CHOICES)


    
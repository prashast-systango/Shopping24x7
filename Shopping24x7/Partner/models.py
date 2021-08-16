from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from constants import *
from Employee.models import Employee, Attendance
from Customer.models import Customer



class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=300)
    partner_name = models.CharField(max_length=200)

class Coupon(models.Model):
    coupon_partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    coupon_name = models.CharField(max_length=200)
    coupon_discount = models.FloatField()

class Location(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, choices=COUNTRY_CHOICES)
    title = models.CharField(max_length=200, choices=TITLE_CHOICES)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    month = models.DateField()

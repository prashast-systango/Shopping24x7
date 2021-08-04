from django.db import models
from django.contrib.auth.models import User
from constants import *

class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    salary = models.IntegerField()
    bank = models.CharField(max_length=200, choices=BANK_CHOICES)  
    bank_account = models.IntegerField()


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    working_hours = models.TimeField()
    required_working_hours = models.TimeField()
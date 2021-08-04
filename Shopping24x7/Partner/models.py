from django.db import models
from django.contrib.auth.models import User
from constants import *
from Employee.models import Employee, Attendance
from Customer.models import Customer
# from django.contrib.auth.models import User, update_last_login
# from django.core.validators import MaxValueValidator, MinValueValidator


# class Customer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     locality = models.CharField(max_length=200)
#     city = models.CharField(max_length=50)
#     zipcode = models.IntegerField()
#     state = models.CharField(max_length=50, choices=STATE_CHOICES)


# def __str__(self):
#     return str(self.id)




class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)




# class OrderPlaced(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     ordered_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50, choices=STATE_CHOICES, default='Pending')

#     def __str__(self):
#         return str(self.id)


class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_name = models.CharField(max_length=200)

    # def __str__(self):
    #     return str(self.id)




class Coupon(models.Model):
    coupon_partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    coupon_name = models.CharField(max_length=200)
    coupon_discount = models.FloatField()


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
#     partner_name = models.CharField(max_length=200)
#     total = models.FloatField()


# class Employee(models.Model):
#     employee_name = models.CharField(max_length=200)
#     department = models.CharField(max_length=200)
#     salary = models.IntegerField()
#     bank = models.CharField(max_length=200, choices=BANK_CHOICES)  
#     bank_account = models.IntegerField()


# class Attendance(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     date = models.DateField()
#     check_in = models.DateTimeField()
#     check_out = models.DateTimeField()
#     working_hours = models.TimeField()
#     required_working_hours = models.TimeField()

class Location(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	# type = models.ForeignKey(User, on_delete=models.CASCADE)
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


# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     amount = models.FloatField()



# class Invoice(models.Model):
# 	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
# 	title = models.ForeignKey(Product, on_delete=models.CASCADE)
# 	description = models.ForeignKey(Product, on_delete=models.CASCADE)
# 	date = models.DateField()
# 	address = models.ForeignKey(Location, on_delete=models.CASCADE)
# 	selling_price = models.ForeignKey(Product, on_delete=models.CASCADE)
# 	tax = models.ForeignKey(Product, on_delete=models.CASCADE)

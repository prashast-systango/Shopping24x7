from django.contrib import admin
from .models import (
    Partner,
    Coupon,
    Location,
    Payroll,
    PartnerEmails,
)
from constants import *

@admin.register(Partner)
class PartnerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','email','partner_name',]

@admin.register(PartnerEmails)
class PartnerEmailsModelAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Coupon)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ['id','coupon_partner','coupon_name','coupon_discount']

@admin.register(Location)
class LocationModelAdmin(admin.ModelAdmin):
    list_display = ['id','customer','employee','country','state','city','address','pincode']

@admin.register(Payroll)
class PayrollModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'attendance', 'month']
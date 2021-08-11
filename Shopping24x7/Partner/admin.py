from django.contrib import admin
from .models import (
    Partner,
    Coupon,
    Location,
    Payroll,
)

# @admin.register(Customer)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','name','locality','city','zipcode','state']

# @admin.register(Product)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ['id','title','selling_price','description','brand','category','product_image']

# @admin.register(Cart)
# class CartModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','product','quantity','coupon']

# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','customer','product','quantity','ordered_date','status']

@admin.register(Partner)
class PartnerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','partner_name']

@admin.register(Coupon)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ['id','coupon_partner','coupon_name','coupon_discount']

# @admin.register(Employee)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display = ['id','employee_name','department','salary','bank','bank_account']

# @admin.register(Attendance)
# class AttendanceModelAdmin(admin.ModelAdmin):
#     list_display = ['id','employee','date','check_in','check_out','working_hours']

@admin.register(Location)
class LocationModelAdmin(admin.ModelAdmin):
    list_display = ['id','customer','employee','country','state','city','address','pincode']

@admin.register(Payroll)
class PayrollModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'attendance', 'month']
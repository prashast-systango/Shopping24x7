from django.contrib import admin
from .models import (
    Employee,
    Attendance,
    EmployeeEmails
)
# Register your models here.

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id','employee_name','email','department','salary','bank','bank_account']

@admin.register(Attendance)
class AttendanceModelAdmin(admin.ModelAdmin):
    list_display = ['id','employee','date','check_in','check_out','working_hours']

@admin.register(EmployeeEmails)
class CustomerEmailsModelAdmin(admin.ModelAdmin):
    list_display = ['email']
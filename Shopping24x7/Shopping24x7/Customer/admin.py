from django.contrib import admin
from .models import (
 Customer,
 CustomerEmails,
)
# Register your models here.


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','email', 'name','locality','city','zipcode','state']

@admin.register(CustomerEmails)
class CustomerEmailsModelAdmin(admin.ModelAdmin):
    list_display = ['email']
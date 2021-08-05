from Shopping24x7.utils import TimeStamp
from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import (
    Cart,
    CartItem,
)
# Register your models here.
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity','coupon']

@admin.register(CartItem)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display=['id', 'product_id', 'quantity', 'amount']

# @admin.register(TimeStamp)
# class CartItemModelAdmin(admin.ModelAdmin):
#     list_display=['id', 'product_id', 'quantity', 'amount']
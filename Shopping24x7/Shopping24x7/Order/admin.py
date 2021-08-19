from django.contrib import admin
from .models import (
 OrderPlaced,  
)
# Register your models here.

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status']
    
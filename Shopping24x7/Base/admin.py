from django.contrib import admin
from Base.models import Product
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','description','brand','category','product_image']
from django.db import models
from constants import *

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
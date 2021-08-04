from django.db import models
from django.contrib.auth.models import User
from Partner.models import Product, Coupon
from constants import *

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    partner_name = models.CharField(max_length=200)
    total = models.FloatField()

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    amount = models.FloatField()

    def __str__(self):
        return str(self.id)

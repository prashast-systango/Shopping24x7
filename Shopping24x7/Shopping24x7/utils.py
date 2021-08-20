from django.db import models
from django.db.models.base import Model
# from datetime import datetime, date
from django.db.models.fields import DateTimeField, IntegerField

# from django.utils.timezone import now
# from datetime import now
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    class Meta:
        abstract = True

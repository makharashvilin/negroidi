from django.db import models
from core.models import BaseModel
import string
import random


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(BaseModel):

    name = models.CharField(max_length=255)
    description = models.TextField()
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    stock_qty = models.PositiveIntegerField(default=0)
    expiration_date = models.DateField(null=True, blank=True)
    barcode = models.CharField(max_length=13, editable=False, unique=True)


    def generate_barcode(self):
        return ''.join(random.choice(string.digits) for _ in range(13))

    def save(self, *args, **kwargs):
        self.barcode = self.generate_barcode()

        return super().save( *args, **kwargs)
    def __str__(self):
        return self.name

from enum import unique

from core.models import BaseModel
from django.contrib.admin.utils import model_ngettext
from products.models import Item
from django.db import models
from django.contrib.auth.models import User



def generate_name():
    prefix = 'P00'
    last_purchase = PurchaseOrder.objects.orderby('-id').first()
    if not last_purchase: return f'{prefix}-0'
    return f'{prefix}-{last_purchase.id + 1}'


class PurchaseOrder(BaseModel):
    name = models.CharField(default=generate_name, max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name


class PurchaseOrderItem(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purchase_items')
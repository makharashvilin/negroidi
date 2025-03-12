from email.policy import default

from django.db.models.functions import Trunc
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PurchaseOrderSerializer, PurchaseOrderItemSerializer
from .models import PurchaseOrder, PurchaseOrderItem
from ..inventory.settings import TEMPLATES


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


    @action(default=True, methods=['post'])
    def validate(self, request, pk):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        if purchase_order.completed:
            return Response({'message':'Purchase Order is already validated'})
        for purchase_item in purchase_order.purchase_items:
            item = purchase_item.item
            item.stock_qty += purchase_item.quantity
            item.save()
        purchase_order.completed = True
        purchase_order.save()
        return Response({'message':'completed'})


class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer

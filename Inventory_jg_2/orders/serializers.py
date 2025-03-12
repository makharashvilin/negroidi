from rest_framework import serializers
from .models import PurchaseOrderItem, PurchaseOrder




class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    purchase_order_display = serializers.StringRelatedField(source='purchase_order',read_only=True)
    purchase_order = serializers.PrimaryKeyRelatedField(queryset=PurchaseOrder.objects.all(), write_only=True)
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'



class PurchaseOrderSerializer(serializers.ModelSerializer):
    purchase_items=PurchaseOrderItemSerializer(read_only=True, many=True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

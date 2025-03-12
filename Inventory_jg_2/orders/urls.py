from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PurchaseOrderViewSet, PurchaseOrderItemViewSet

router = DefaultRouter(use_regex_path=False)
router.register('purchaseorder', PurchaseOrderViewSet)
router.register('purchaseorderitem', PurchaseOrderItemViewSet)

urlpatterns = router.urls

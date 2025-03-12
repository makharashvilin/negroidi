from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from products.views import ItemViewSet, CategoryViewSet

router = DefaultRouter(use_regex_path=False)
router.register('items', ItemViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls

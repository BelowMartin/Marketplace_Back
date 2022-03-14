from email.mime import base
from posixpath import basename
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PhotoViewSet, OrderViewSet, UserOrderViewSet

router = SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('photo', PhotoViewSet, basename='photo')
router.register('order', OrderViewSet, basename='order')
router.register('favourite', UserOrderViewSet, basename='favourite')
urlpatterns = router.urls 
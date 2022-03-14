from unicodedata import category
from django import views
from rest_framework import generics, viewsets
from .models import  Order, User, Photo, UserOrder
from .serializers import UserOrderSerializer, UserSerializer, PhotoSerializer, OrderSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserOrderViewSet(viewsets.ModelViewSet):
    serializer_class = UserOrderSerializer

    def get_queryset(self):
        queryset = UserOrder.objects.all()
        user_param = self.request.GET.get('userId')
        order_param = self.request.GET.get('orderId')
        if user_param:
            queryset = queryset.filter(user_id=user_param)
        
        if order_param:
            queryset = queryset.filter(order_id=order_param)
        
        return queryset

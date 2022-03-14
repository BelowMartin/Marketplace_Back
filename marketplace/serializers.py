from dataclasses import field, fields
from rest_framework import serializers
from .models import Order, User, Photo, UserOrder

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 
            'name', 'surname', 
            'phone'
             )

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = (
            'id', 'url'
        )

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id', 'user_id', "photo_id",
            'name', 'from_to', 'where_to',
            'date', 'price', 'award'
        )
        depth = 1

class UserOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserOrder
        fields = (
            'user_id', 'order_id'
        )

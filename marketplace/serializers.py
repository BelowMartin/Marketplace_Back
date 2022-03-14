from dataclasses import field, fields
from rest_framework import serializers
from .models import User, Photo

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

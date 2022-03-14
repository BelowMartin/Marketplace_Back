from unicodedata import category
from django import views
from rest_framework import generics, viewsets
from .models import  User, Photo
from .serializers import UserSerializer, PhotoSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
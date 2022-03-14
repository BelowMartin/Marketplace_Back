from django.contrib import admin
from .models import User, Photo, Order, UserOrder

# Register your models here.
admin.site.register([
    User, Photo, Order, UserOrder
])
from django.contrib import admin
from .models import User, Photo

# Register your models here.
admin.site.register([
    User, Photo
])
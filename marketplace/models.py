from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.url

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

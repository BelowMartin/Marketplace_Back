from statistics import mode
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

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
    name = models.TextField()
    from_to = models.CharField(max_length=100)
    where_to = models.CharField(max_length=100)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    award = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class UserOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)
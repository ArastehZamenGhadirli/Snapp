from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDirection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    origin_x = models.CharField(max_length=50)
    origin_y = models.CharField(max_length=50)
    destination_x = models.CharField(max_length=50)
    destination_y = models.CharField(max_length=50)
    bearing = models.FloatField()
    payment = models.IntegerField()
    initial_amount = models.FloatField(default=1000000)
    


class UserWallet(User):
    wallet = models.PositiveIntegerField(default = 10_000_000)




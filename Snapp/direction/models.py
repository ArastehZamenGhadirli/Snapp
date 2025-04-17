from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDirection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    origin_x = models.FloatField()
    origin_y = models.FloatField()
    destination_x = models.FloatField()
    destination_y = models.FloatField()
    bearing = models.FloatField()
    payment = models.IntegerField()
    initial_amount = models.IntegerField(default=1000000)


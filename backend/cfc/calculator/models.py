from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class dailyData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    lpg = models.IntegerField(default=0)
    petrol = models.IntegerField(default=0)
    diesel = models.IntegerField(default=0)
    electricity = models.IntegerField(default=0)
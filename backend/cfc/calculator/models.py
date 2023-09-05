from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
# Create your models here.

class dailyData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    lpg = models.IntegerField(default=0)
    petrol = models.IntegerField(default=0)
    diesel = models.IntegerField(default=0)
    electricity = models.IntegerField(default=0)

    @classmethod
    def get_last_7_days_data(cls, user):
        # Calculate the date 7 days ago from today
        seven_days_ago = date.today() - timedelta(days=7)

        # Query the database for data in the last 7 days for the specified user
        data = cls.objects.filter(user=user, date__gte=seven_days_ago, date__lte=date.today()).order_by('date')

        # Create a dictionary to store data for each day
        data_dict = {str(seven_days_ago + timedelta(days=i)): 0 for i in range(7)}

        # Fill in the dictionary with actual data
        for entry in data:
            data_dict[str(entry.date)] = sum([entry.lpg, entry.petrol, entry.diesel, entry.electricity])  # Change this to the appropriate field


        return data_dict

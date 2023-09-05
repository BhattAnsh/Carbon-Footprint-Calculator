from datetime import date, time
from .models import *
from . import views






class last_seven_days_data:
    def __init__(self, username):
        self.user = username
        self.cfc_data = {}

    def mappingDays(self, dict):
        data_list = []
        current_date= date.today()
        current_date = date.today()

        date_list = []

        for i in range(7):
            day = current_date - timedelta(days=i)
            date_list.append(day.strftime('%Y-%m-%d'))
        for j in date_list:
            if j in dict:
                data_list.append(dict[j])
            else: 
                data_list.append(0)
        print(date_list)
        return data_list


    def gettingDaysAndData(self):
        current_date = date.today()
        last_7_days_data_dict = dailyData.get_last_7_days_data(self.user)
        last_7_days_data = self.mappingDays(last_7_days_data_dict)
        last_seven_days_names = []

        for i in range(7):
            day = current_date - timedelta(days=i)
            
            day_name = day.strftime('%A')
            last_seven_days_names.append(day_name)
        print(last_seven_days_names)

        return last_7_days_data, last_seven_days_names
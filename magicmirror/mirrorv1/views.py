import requests
from django.shortcuts import render

def getWeekDayName(day_of_week):
    days_of_week = {
        1 : 'Monday',
        2: 'Tuesday',
        3 : 'Wednesday',
        4 : 'Thursday',
        5 : 'Friday',
        6 : 'Saturday',
        7 : 'Sunday'
    }
    if day_of_week in days_of_week:
        return days_of_week.get(day_of_week)
   
def index(request):
    url = 'http://worldtimeapi.org/api/timezone/{}'
    region = '/America/Argentina/Salta'

    r = requests.get(url.format(region)).json()

    city_time = {
        'day_of_year' : r['day_of_year'],
        'day_of_week' : getWeekDayName(r['day_of_week']),
        'datetime' : r['datetime']
    }

    context = {'city_time' : city_time}
    return render(request, 'timezone/timezone.html', context)


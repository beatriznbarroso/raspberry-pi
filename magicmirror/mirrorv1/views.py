import requests
from django.shortcuts import render
import datetime
   
def index(request):
    city_time = {
        'current_hour' : datetime.datetime.now().strftime('%H:%M:%S'),
        'week_day' : getWeekDayName(datetime.datetime.now().isoweekday()),
        'datetime' : datetime.datetime.now()

    }
    weather = getWeather(request)
    return render(request, 'mirrorv1/index.html', context = {'city_time' : city_time, 'weather' : weather})

def getWeekDayName(day_of_week):
    days_of_week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    if day_of_week in days_of_week:
        return days_of_week.get(day_of_week)
    else:
        return "I have no clue what day of the week it is"


def getWeather(request):
    city = 'Lisbon'

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=89b538f7c4e57f23da6886ac03629e15&units=metric'.format(
        city)

    res = requests.get(url)

    data = res.json()
    weather = {
        'description': data['weather'][0]['description'],
        'temp': data['main']['temp'],
        'temp_min': data['main']['temp_min'],
        'temp_max': data['main']['temp_max'],
        'icon': data['weather'][0]['icon']
    }

    return weather

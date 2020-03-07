import requests
import datetime
from django.shortcuts import render
from newsapi import NewsApiClient

   
def index(request):
    city_time = {
        'current_hour' : datetime.datetime.now().strftime('%H:%M:%S'),
        'week_day' : getWeekDayName(datetime.datetime.now().isoweekday()),
        'datetime' : datetime.datetime.now()
    }
    getNews()
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

def getNews() :
    # Init
    newsapi = NewsApiClient(api_key='8cef481256e4410fbacdad418e928efc')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge',
                                            language='en',
                                            page_size=5)

    # /v2/everything
    # all_articles = newsapi.get_everything(q='bitcoin',
    #                                     sources='bbc-news,the-verge',
    #                                     domains='bbc.co.uk,techcrunch.com',
    #                                     from_param='2017-12-01',
    #                                     to='2017-12-12',
    #                                     language='en',
    #                                     sort_by='relevancy',
    #                                     page=2)

    # /v2/sources
    # sources = newsapi.get_sources()
    return top_headlines

import requests

city = input('Enter your city: ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=89b538f7c4e57f23da6886ac03629e15&units=metric'.format(
    city)

res = requests.get(url)

data = res.json()
weather = {
    'description': data['weather'][0]['description'],
    'temp': data['main']['temp'],
    'temp_min': data['main']['temp_min'],
    'temp_max': data['main']['temp_max']
}


print(weather)

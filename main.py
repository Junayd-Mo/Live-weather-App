import datetime as dt, requests


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = '68d53a3d6c13a5dffe24dd43ecc44831'
CITY = 'London'
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
print(response)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15 
    return celsius

def temperature():
    temp = round(kelvin_to_celsius(response['main']['temp']),1)
    return temp

def Weather_description():
    description = response['weather'][0]['description'].title()
    return description

def min_temp():
    minimum_temperature = round(kelvin_to_celsius(response['main']['temp_min']),1)
    return minimum_temperature

def max_temp():
    maximum_temperature = round(kelvin_to_celsius(response['main']['temp_max']),1)
    return maximum_temperature

def visibility():
    visible = response['visibility']
    return visible

def humidity():
    humid_level = response['main']['humidity']
    return humid_level

def windSpeed():
    wind_speed = response['wind']['speed']
    return wind_speed



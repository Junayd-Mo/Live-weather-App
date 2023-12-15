from flask import Flask, render_template,request, flash
from main import temperature,Weather_description ,min_temp,max_temp,humidity,visibility,windSpeed
import requests

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'Secret Key'

temp = temperature()
description = Weather_description()
temp_min = min_temp()
temp_max = max_temp()
humid = humidity()
wind = windSpeed()
visible = visibility()
city_name = 'London'


@app.route('/')
def index():
    return render_template('index.html', visible=visible,wind=wind,humid=humid,city_name=city_name,temp=temp, description=description,temp_min=temp_min,temp_max=temp_max)

@app.route('/city',methods = ['GET', 'Post'])
def city():
    if request.method == 'POST':
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = '68d53a3d6c13a5dffe24dd43ecc44831'
        
        CITY = request.form['city'].title()
        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY


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
        try:
            response = requests.get(url).json()
            temp = temperature()
            description = Weather_description()
            temp_min = min_temp()
            temp_max = max_temp()
            humid = humidity()
            wind = windSpeed()
            visible = visibility()
        except: 
            return 'Location is spelt incorrectly or does not exist Please select return to go back to the main page'
        return render_template('index.html',visible=visible,wind=wind,humid=humid,city=CITY,temp=temp, description=description,temp_min=temp_min,temp_max=temp_max)



if __name__ =='__main__':
    app.run(debug=True)
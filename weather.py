import requests
import json
API="Generate API from openweathermap.com and enter API key here"
lat= #Enter Latitude Value
long= #Enter Longitudinal Value
def printWeather():

    url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API}"

    response=requests.get(url)
    x=response.json()
    if x['cod'] != '404':
        y=x['main']
        temperature=y['temp']
        pressure=y['pressure']
        humidity=y['humidity']
        max_temp=y['temp_max']
        min_temp=y['temp_min']

        z=x['weather']

        description = z[0]["description"]
        print(f"Description: {str(description)}\nTemperature: {str(round(temperature-273.15))} degree celsius\nAtmospheric Pressure: {str(pressure)}hpa\nHumidity: {str(humidity)}%")


    else:
        print('City Not Found !!!')

printWeather()

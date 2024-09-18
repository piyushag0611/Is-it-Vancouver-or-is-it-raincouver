import requests
import json

def get_weather():

    base_url = 'https://api.weather.gc.ca/collections/climate-hourly/items'
    complete_url = f'{base_url}?&bbox=-123.264,49.002,-122.313,49.494&LOCAL_YEAR=2024&LOCAL_MONTH=8&PROVINCE_CODE=BC'
    response = requests.get(complete_url)
    weather_data = response.json()
    print(weather_data['numberMatched'])

get_weather()
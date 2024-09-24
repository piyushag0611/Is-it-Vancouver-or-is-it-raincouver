import requests
import json


def get_weather():

    base_url = 'https://api.weather.gc.ca/collections/climate-hourly/items'
    entries = []
    for year in range(2014, 2024):
        for month in range(1, 13):
            complete_url = f'{base_url}?&bbox=-123.264,49.002,-122.313,49.494&LOCAL_YEAR={year}&LOCAL_MONTH={month}&PROVINCE_CODE=BC'
            response = requests.get(complete_url)
            weather_data = response.json()
            entries.append(weather_data['numberMatched'])
    print(max(entries), min(entries), sum(entries))

get_weather()
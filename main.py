import requests
import json


def getWeather(city:str):
    api_key = '29af92d9f93c8cf795be3ab8bb4f6776'

    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q":city,
        "appid": api_key,
    }

    r = requests.get(url, params=params)
    data = r.json()
    return data
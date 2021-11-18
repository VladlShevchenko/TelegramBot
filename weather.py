import json
import requests
from pprint import pprint
from datetime import datetime

APPID = '2f6df4e456d2fa62cf6d19b557ee5356'
URL_BASE = "http://api.openweathermap.org/data/2.5/"
lang = "ua"
units = "metric"


def current_weather(q: str =  "Chicago", appid: str = APPID, units: str = units) -> dict:#текущяя погода
    data =  requests.get(URL_BASE+"weather", params=locals()).json()

    return f'Temperature: {data["main"]["temp"]}, Feels like: {data["main"]["feels_like"]}, Wind: {data["wind"]["speed"]}'
   

def weather_forecast(q: str = "Chicago", appid: str = APPID) ->dict:#прогноз погоды
    data = requests.get(URL_BASE+"forecast", params=locals()).json()
    with open ("chat-bot\\forecast.json", "w") as json_file:
        json.dump(data, json_file, indent=2)
    return data



def weather_onecall(lat: float = 55.68, lon: float = 12.57, appid: str = APPID) -> dict:#json по локации
    data = requests.get(URL_BASE+"onecall", params=locals()).json()
    with open ("chat-bot\onecall.json", "w") as json_file:
        json.dump(data, json_file, indent=2)
    
    return data

if __name__ == "__main__":
    while True: 
        location = input("Enter a location: ").strip()
        if location: 
            pprint(current_weather(location))
        else: 
            break
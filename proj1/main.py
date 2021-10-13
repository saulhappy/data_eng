import pandas as pd
import requests
import json
import os

from creds.keys import KEYS
from constants import URL, HOST

os.system('cls' if os.name == 'nt' else 'clear')

url = URL

querystring = {"units":"auto","lang":"en"}

headers = {
    'x-rapidapi-host': HOST,
    'x-rapidapi-key': KEYS["x-rapidapi-key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()

summary = data["daily"]["summary"]
time = data["daily"]["data"][0]["time"]
sunrise_time = data["daily"]["data"][0]["sunriseTime"]
sunset_time = data["daily"]["data"][0]["sunsetTime"]
temp_high = data["daily"]["data"][0]["temperatureHigh"]
temp_low = data["daily"]["data"][0]["temperatureLow"]
humidity = data["daily"]["data"][0]["humidity"]

print(summary, time, sunrise_time, sunrise_time, temp_high, temp_low, humidity)




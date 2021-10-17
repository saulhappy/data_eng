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

weather_data = {}

weather_data["summary"] = summary
weather_data["time"] = time
weather_data["sunrise_time"] = sunrise_time
weather_data["sunset_time"] = sunset_time
weather_data["temp_high"] = temp_high
weather_data["temp_low"] = temp_low
weather_data["humidity"] = humidity

weather_data_frame = pd.DataFrame(weather_data, columns=["summary", "time", "sunrise_time", "sunset_time", "temp_high", "temp_low", "humidity"], index=[0])

def validate_data_frame(weather_data_frame):
    # validate not empty
    if weather_data_frame.empty:
        raise Exception("Data frame is empty.")
    
    # check primary key uniqueness
    if not pd.Series(weather_data_frame["time"]).is_unique:
        raise Exception("Primary key constraint violated")
    
    # check for nulls
    if weather_data_frame.isnull().values.any():
        raise Exception("Null values found")
    
    return True

if validate_data_frame(weather_data_frame):
    print("All data checks passed!")
        

print(weather_data_frame)

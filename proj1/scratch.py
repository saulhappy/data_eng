import pandas as pd
import requests
import json
import os

from constants import URL, QUERY_STRING, HEADERS

os.system('cls' if os.name == 'nt' else 'clear')


response = requests.request("GET", URL, headers=HEADERS, params=QUERY_STRING)
data = response.json()

timestamp = data["response"][0]["periods"][0]["timestamp"]
max_temp_f = data["response"][0]["periods"][0]["maxTempF"]
min_temp_f = data["response"][0]["periods"][0]["minTempF"]
max_humidity = data["response"][0]["periods"][0]["maxHumidity"]
min_humidity = data["response"][0]["periods"][0]["minHumidity"]
precip_in = data["response"][0]["periods"][0]["precipIN"]
weather = data["response"][0]["periods"][0]["weather"]
sunrise = data["response"][0]["periods"][0]["sunrise"]
sunset = data["response"][0]["periods"][0]["sunset"]


weather_data = {}

weather_data["timestamp"] = timestamp
weather_data["max_temp_f"] = max_temp_f
weather_data["min_temp_f"] = min_temp_f
weather_data["max_humidity"] = max_humidity
weather_data["min_humidity"] = min_humidity
weather_data["precip_in"] = precip_in
weather_data["weather"] = weather
weather_data["sunrise"] = sunrise
weather_data["sunset"] = sunset


weather_data_frame = pd.DataFrame(weather_data, columns=["timestamp", "max_temp_f", "min_temp_f", "max_humidity", "min_humidity", "precip_in", "weather", "sunrise", "sunset"], index=[0])

def validate_data_frame(weather_data_frame):
    # validate not empty
    if weather_data_frame.empty:
        raise Exception("Data frame is empty.")
    
    # check primary key uniqueness
    if not pd.Series(weather_data_frame["timestamp"]).is_unique:
        raise Exception("Primary key constraint violated")
    
    # check for nulls
    if weather_data_frame.isnull().values.any():
        raise Exception("Null values found")
    
    return True

if validate_data_frame(weather_data_frame):
    print("All data checks passed!")
        

print(weather_data_frame)

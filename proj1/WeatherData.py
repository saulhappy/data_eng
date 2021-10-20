import pandas as pd
import requests

from constants import URL, HEADERS, QUERY_STRING

class WeatherData():
    def __init__(self):
        self.data = {}

    def query_api(self):
        response = requests.request("GET", URL, headers=HEADERS, params=QUERY_STRING)
        return response.json()

    def format_data(self):
        data = self.query_api()

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

        self.data = weather_data

    def get_formatted_data(self):
        return self.data
    
    def get_data_frame_from_formatted_data(self):
        fd = self.get_formatted_data()
        data_frame = pd.DataFrame(fd, columns=["timestamp", "max_temp_f", "min_temp_f", "max_humidity", "min_humidity", "precip_in", "weather", "sunrise", "sunset"], index=[0])
        return data_frame
    
    










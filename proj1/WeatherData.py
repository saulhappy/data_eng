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

        summary = data["daily"]["summary"]
        time = data["daily"]["data"][0]["time"]
        sunrise_time = data["daily"]["data"][0]["sunriseTime"]
        sunset_time = data["daily"]["data"][0]["sunsetTime"]
        temp_high = data["daily"]["data"][0]["temperatureHigh"]
        temp_low = data["daily"]["data"][0]["temperatureLow"]
        humidity = data["daily"]["data"][0]["humidity"]

        formated_data = {
            "summary": summary,
            "time" : time,
            "sunrise_time": sunrise_time,
            "sunset_time": sunset_time,
            "temp_high": temp_high,
            "temp_low": temp_low,
            "humidity": humidity
        }
        self.data = formated_data

    def get_formatted_data(self):
        return self.data
    
    def get_data_frame_from_formatted_data(self):
        fd = self.get_formatted_data()
        data_frame = pd.DataFrame(fd, columns=["summary", "time", "sunrise_time", "sunset_time", "temp_high", "temp_low", "humidity"], index=[0])
        return data_frame
    
    










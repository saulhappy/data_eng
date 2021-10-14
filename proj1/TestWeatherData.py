import unittest
import json
import requests

from WeatherData import WeatherData
from constants import URL, HEADERS, QUERY_STRING

class TestWeatherData(unittest.TestCase):
    response = requests.request("GET", URL, headers=HEADERS, params=QUERY_STRING)

    def setUp(self):
        self.weather_data = WeatherData()

    def test_WeatherDataCreate(self):
         self.assertIsInstance(self.weather_data, WeatherData)
    
    def test_query_api(self):
        data = self.response.json()
        self.assertIn("daily", data)

    def test_get_formatted_data(self):
        wd = WeatherData()
        wd.format_data()
        data = wd.get_formatted_data()
        self.assertIn("summary", data)
        self.assertIn("time", data)
        self.assertIn("sunrise_time", data)
        self.assertIn("sunset_time", data)
        self.assertIn("temp_high", data)
        self.assertIn("temp_low", data)
        self.assertIn("humidity", data)



if __name__ == "__main__":
    unittest.main()
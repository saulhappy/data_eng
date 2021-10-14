import unittest
import json
import requests

from WeatherData import WeatherData
from constants import URL, HEADERS, QUERY_STRING

class TestWeatherData(unittest.TestCase):

    def setUp(self):
        self.weather_data = WeatherData()

    def test_WeatherDataCreate(self):
         self.assertIsInstance(self.weather_data, WeatherData)
    
    def test_query_api(self):
        response = requests.request("GET", URL, headers=HEADERS, params=QUERY_STRING)
        data = response.json()
        self.assertIn("daily", data)


if __name__ == "__main__":
    unittest.main()
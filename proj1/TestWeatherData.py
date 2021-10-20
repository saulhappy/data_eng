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
        self.assertEqual(data["success"], True)

    def test_get_formatted_data(self):
        wd = WeatherData()
        wd.format_data()
        data = wd.get_formatted_data()
        self.assertIn("timestamp", data)
        self.assertIn("max_temp_f", data)
        self.assertIn("min_temp_f", data)
        self.assertIn("max_humidity", data)
        self.assertIn("min_humidity", data)
        self.assertIn("precip_in", data)
        self.assertIn("weather", data)
        self.assertIn("sunrise", data)
        self.assertIn("sunset", data)
    
    def test_get_data_frame_from_formatted_data(self):
        wd = WeatherData()
        wd.format_data()
        data_frame = wd.get_data_frame_from_formatted_data()
        self.assertEqual(len(data_frame), 1)

if __name__ == "__main__":
    unittest.main()
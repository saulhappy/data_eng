import pandas as pd
import requests
import json
import os

from collections import defaultdict
from constants import URL, HEADERS, QUERY_STRING

class WeatherData():
    def __init__(self):
        self.data = defaultdict

    def query_api(self):
        response = requests.request("GET", URL, headers=HEADERS, params=QUERY_STRING)
        return response.json()

    def format_data(self):
        pass








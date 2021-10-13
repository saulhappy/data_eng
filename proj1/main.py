import pandas as pd
import requests
import json

from creds.keys import KEYS
from constants import URL, HOST


url = URL

querystring = {"units":"auto","lang":"en"}

headers = {
    'x-rapidapi-host': HOST,
    'x-rapidapi-key': KEYS["x-rapidapi-key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




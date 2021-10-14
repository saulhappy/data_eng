from creds.keys import KEYS

LAT = 30.360090
LONG = -97.692980

URL = f"https://dark-sky.p.rapidapi.com/{LAT},{LONG}"
HOST = "dark-sky.p.rapidapi.com"
QUERY_STRING = {"units":"auto","lang":"en"}

HEADERS = {
    'x-rapidapi-host': HOST,
    'x-rapidapi-key': KEYS["x-rapidapi-key"]
}
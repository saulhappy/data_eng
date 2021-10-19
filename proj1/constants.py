from creds.keys import KEYS

LAT = 30.360090
LONG = -97.692980

URL = "https://aerisweather1.p.rapidapi.com/forecasts/78748"
HOST = "aerisweather1.p.rapidapi.com"
QUERY_STRING = {"radius":"10"}

HEADERS = {
    'x-rapidapi-host': HOST,
    'x-rapidapi-key': KEYS["x-rapidapi-key"]
}

import os
import requests
from dotenv import load_dotenv

load_dotenv()

tequilla_endpoint = os.getenv("TEQUILLA_ENDPOINT")
header = {
    "apikey": os.getenv("TEQUILLA_API_KEY")
}


class FlightSearch:

    def flight_search(self, city):

        params = {
            "term": city
        }
        response = requests.get(url=tequilla_endpoint, headers=header, params=params)
        response.raise_for_status()
        return response.json()['locations'][0]['code']

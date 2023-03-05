import os
import requests
from datetime import datetime, timedelta

from dotenv import load_dotenv

load_dotenv()

tequilla_endpoint = os.getenv("TEQUILLA_SEARCH_ENDPOINT")
header = {
    "apikey": os.getenv("TEQUILLA_API_KEY")
}

class FlightData:

    def __init__(self):
        self.fly_from = "HYD"
        self.today = datetime.now()
        self.current_date = self.today + timedelta(days=1)
        self.current_date = self.current_date.strftime("%d/%m/%Y")
        self.next_date = datetime.now() + timedelta(days=365)
        self.final_date = self.next_date.strftime("%d/%m/%Y")
        self.min_return_date = self.next_date + timedelta(days=12)
        self.min_return_date = self.min_return_date.strftime("%d/%m/%Y")
        self.max_return_date = self.next_date + timedelta(days=35)
        self.max_return_date = self.max_return_date.strftime("%d/%m/%Y")

    def flight_cost(self, city):
        params = {
            "fly_from": self.fly_from,
            "fly_to": city,
            "date_from": self.current_date,
            "date_to": self.final_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "INR",
            "sort": "price",
        }
        response = requests.get(url=tequilla_endpoint, headers=header, params=params)
        response.raise_for_status()
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {city}")
            return "None"
        return data['price']

import os
import requests
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

sheety_project_name = os.getenv("SHEETY_PROJECT_NAME")
sheety_project_sheet = os.getenv("SHEETY_PROJECT_SHEET")
sheety_app_key = os.getenv("SHEETY_API_KEY")
sheety_endpoint = f"https://api.sheety.co/{sheety_app_key}/{sheety_project_name}/{sheety_project_sheet}"
sheety_headers = {
    "Authorization": os.getenv("SHEETY_AUTH")
}

class DataManager:

    def google_sheet_data(self):

        response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        return response.json()


    def update_iata_code(self, code, i):

        sheety_data = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(url=sheety_endpoint+f"/{i}", json=sheety_data, headers=sheety_headers)
        print(response.json())

    def update_lowest_price(self, price, i):

        sheety_data = {
            "price": {
                "lowestPrice": price
            }
        }
        response = requests.put(url=sheety_endpoint+f"/{i}", json=sheety_data, headers=sheety_headers)
        print(response.json())

    def add_user(self, first_name, last_name, email):
        sheety_project_sheet = os.getenv("SHEETY_PROJECT_SHEET_2")
        sheety_endpoint = f"https://api.sheety.co/{sheety_app_key}/{sheety_project_name}/{sheety_project_sheet}"

        sheety_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_headers)
        print(response.json())


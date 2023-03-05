#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

from pprint import pprint


# File Imports
sheet_data = DataManager()
flight_iata = FlightSearch()
flight_data = FlightData()
notification = NotificationManager()
data = sheet_data.google_sheet_data()


print("Welcome to Flight Club.")
print("We find the best flight deals and email you.")
prompt = input("Do you want to join Flight Club? Type 'yes' or 'no'.")
if prompt.lower() == "yes":
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email = input("What is your email? ")
    email_check = input("Type your email again. ")
    if email == email_check:
        sheet_data.add_user(first_name, last_name, email)
        print("You have been added to our mailing list.")

for i in range(0, len(data['prices'])):
    city = data['prices'][i]['city']
    iata_code = flight_iata.flight_search(city)
    sheet_data.update_iata_code(iata_code, i+2)
    cost = flight_data.flight_cost(iata_code)
    if cost != "None":
        if cost < data['prices'][i]['lowestPrice']:
            sheet_data.update_lowest_price(cost, i+2)
            message = f"Low price alert! Only ₹{cost} to fly from Hyderabad to {data['prices'][i]['city']}, from {flight_data.current_date} to {flight_data.min_return_date}."
            notification.send_sms(f"Low price alert! Only ₹{cost} to fly from Hyderabad to {data['prices'][i]['city']}, from {flight_data.current_date} to {flight_data.min_return_date}.")
    else:
        sheet_data.update_lowest_price("None", i+2)
    data = sheet_data.google_sheet_data()
    pprint(f"{data['prices'][i]['city']} : ₹{cost}")

import os
import requests
import smtplib
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

# Twilio API Config
twilio_accid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_authtoken = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(twilio_accid, twilio_authtoken)


class NotificationManager:

    def send_sms(self, message):
        message = client.messages \
            .create(
            body=message,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=os.getenv("MY_PHONE_NUMBER")
        )
        print(message.status)

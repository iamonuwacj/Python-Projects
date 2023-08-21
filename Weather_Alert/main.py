import requests
import os
from twilio.rest import Client

auth_token = ""
account_sid = ""
weather_api = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = ""

parameters = {
    "lat": 5.038963,
    "lon": 7.909470,
    "appid": API_KEY
}
response = requests.get(url=weather_api, params=parameters)
response.raise_for_status()

weather_data = response.json()["list"]
will_rain = False
for data in weather_data:
    weather_id = data["weather"][0]["id"]
    if int(weather_id) < 800:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today, remember to bring an umbrella.",
        from_='+14704584215',
        to='+2348140154374',
    )
    print(message.status)
else:
    print("Sunny Day")

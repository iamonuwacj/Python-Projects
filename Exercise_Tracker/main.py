from dotenv import load_dotenv, find_dotenv
import requests
import os
from datetime import *

load_dotenv(find_dotenv())
app_id = os.environ.get("APP_ID")
api_key = os.environ.get("API_KEY")
Sheety_Get_Endpoint = "https://api.sheety.co/1d0ad6dbe9dede84297b885820775630/workoutTraining/workouts"
Sheety_Post_Endpoint = "https://api.sheety.co/1d0ad6dbe9dede84297b885820775630/workoutTraining/workouts"

api_headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
    "x-remote-user-id": "0"
}
API_Exercise_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which exercise you did: \n")

json_parameters = {
    "query": query,
    "gender": "male",
    "age": 30,
}
time = datetime.now().strftime("%H:%M:%S")
today = date.today().strftime("%d/%m/%Y")

response = requests.post(url=API_Exercise_Endpoint, json=json_parameters, headers=api_headers)
data = response.json()["exercises"]

auth_token = os.environ.get("AUTH_TOKEN")

sheety_header = {
    "Authorization": auth_token,
}

for dict_data in data:
    exercise = dict_data["name"]
    duration = dict_data["duration_min"]
    calories = dict_data["nf_calories"]

    Sheety_add_parameters = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }
    sheety_response = requests.post(url=Sheety_Post_Endpoint, json=Sheety_add_parameters, headers=sheety_header)
print("Activity Logged. ")


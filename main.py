import requests
import datetime as dt
import os

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

NUTRI_ID = os.environ.get("NUTRI_ID")
NUTRI_KEY = os.environ.get("NUTRI_KEY")
AUTHORIZATION = os.environ.get("AUTHORIZATION")

GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")

TODAY = dt.date.today().strftime("%d/%m/%y")
TIME = dt.datetime.now().strftime("%H:%M:%S")

headers = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_KEY,
    "authorization": AUTHORIZATION,
}

exercise_params = {
    "query": input("What exercise did you do today?: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(NUTRI_ENDPOINT, json=exercise_params, headers=headers)
workout_data = response.json()

for workout in workout_data["exercises"]:
    new_row = {
        "workout": {
            "date": TODAY,
            "time": TIME,
            "exercise": workout["name"],
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }
    response = requests.post(url=SHEET_ENDPOINT, json=new_row)
    print(response.text)

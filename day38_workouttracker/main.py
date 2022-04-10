import requests
from datetime import datetime

exercise_endpoint = "GET YOUR OWN ENDPOINT"
sheet_endpoint = "GET YOUR OWN ENDPOINT"

user_input = input("Tell me which exercise you did: ")

header = {
    "x-app-id": "GET YOUR OWN API KEY",
    "x-app-key": "GET YOUR OWN API KEY",
}

params = {
    "query": user_input
}

response = requests.post(url=exercise_endpoint, json=params, headers=header)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

print(sheet_response.text)







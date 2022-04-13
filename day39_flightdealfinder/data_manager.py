import requests
from pprint import pprint

SHEET_ENDPOINT = "https://api.sheety.co/264fea7b29b51400315205328912d44e/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        pprint(self.destination_data)

    def update_destination_data(self):
        for city in self.destination_data:
            sheet_input = {
                "price": {
                    "iataCode": "Testing"
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=sheet_input)
            print(response.text)

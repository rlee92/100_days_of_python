import requests

parameters = {
    "lat": "ENTER YOUR LAT",
    "lon": "ENTER YORU LON",
    "exclude": "current,minutely,daily",
    "appid": "ENTER YOUR API KEY"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

weather_slice = data["hourly"][::]

will_rain = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

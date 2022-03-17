import requests
import datetime

MY_LAT = 51.507351
MY_LNG = -0.127758


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.datetime.now()
print(sunrise.split("T"))
print(sunset)

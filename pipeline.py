#sraddha's code for 4.1/4.2


import requests

BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": 30.44,
    "longitude": -84.28, #this is lat/long for tallahassee
    "start_date": "2026-03-23",
    "end_date": "2026-04-06",
    "hourly": "temperature_2m",
    "temperature_unit": "fahrenheit",
    "wind_speed_unit": "mph",
    "precipitation_unit": "inch"
}



response = requests.get(BASE_URL, params=params, timeout=10)

print("Status:", response.status_code)

data = response.json()

records = []

hourly = data.get("hourly", {})

times = hourly.get("time", [])
temps = hourly.get("temperature_2m", [])



for i in range(len(times)):
    record = {
        "time": times[i] if i < len(times) else None,
        "temperature": temps[i] if i < len(temps) else None,
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "timezone": data.get("timezone", "Unknown")
    }
    records.append(record)

print(records[:5])  #prints 1st 5 rows, can be removed if ned be










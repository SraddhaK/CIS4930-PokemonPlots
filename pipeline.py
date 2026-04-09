#sraddha's code for 4.1/4.2
# sam's code as well for 4.3 (error handling)

import requests
import logging

logging.basicConfig(
    filename = "pipeline_error.log",
    level = logging.ERROR,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

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

retry_flag = 2   # 1 to retry (1 time if Timeout exception)

# Error checking, for loop to retry upon Timeout exception
while retry_flag > 0:

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout:
        retry_flag -= 1     # decrements retry_flag so if this has already retried it will not loop again
        message = "Request timed out, will skip this run"
        print(message)
        logging.error(message)
    except requests.exceptions.RequestException as e:
        retry_flag = 0
        message = f"request error: {e}"
        print(message)
        logging.error(message)
    else:
        retry_flag = 0
        if response.status_code == 200:
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

            print(records[:5])  #prints 1st 5 rows, can be removed if need be










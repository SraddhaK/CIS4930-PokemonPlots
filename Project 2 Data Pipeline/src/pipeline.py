#sraddha's code for 4.1/4.2
# sam's code as well for 4.3 (error handling)
# aiden's code as well for 4.4 (repeated calls and automation)

import requests
import logging
import os
from datetime import date, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "pipeline_error.log"),
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

# Multiple cities to loop over and aggregate results
cities = [
    {"name": "Tallahassee, FL", "latitude": 30.44, "longitude": -84.28},
    {"name": "Miami, FL",       "latitude": 25.77, "longitude": -80.19},
    {"name": "Orlando, FL",     "latitude": 28.54, "longitude": -81.38},
]

yesterday = date.today() - timedelta(days=1)

# Define parameters to pull data from and make API calls to
base_params = {
    "start_date": yesterday.isoformat(),
    "end_date": yesterday.isoformat(),
    "hourly": "temperature_2m",
    "temperature_unit": "fahrenheit",
    "wind_speed_unit": "mph",
    "precipitation_unit": "inch"
}

all_records = []  # Aggregated results across all cities

for city in cities:
    print(f"DEBUG: city variable is -> {city}")  # Add this line
    print(f"Fetching data for {city['name']}...")

    params = {
        **base_params,
        "latitude": city["latitude"],
        "longitude": city["longitude"],
    }

    retry_flag = 2 # 1 to retry (1 time if Timeout exception)

    # Error checking, for loop to retry upon Timeout exception
    while retry_flag > 0:
        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

        except requests.exceptions.Timeout:
            retry_flag -= 1
            message = f"Request timed out for {city['name']}, will skip this run"
            print(message)
            logging.error(message)

        except requests.exceptions.RequestException as e:
            retry_flag = 0
            message = f"Request error for {city['name']}: {e}"
            print(message)
            logging.error(message)

        # On successful requests, start getting data 
        else:
            retry_flag = 0
            if response.status_code == 200:
                hourly = data.get("hourly", {})
                times = hourly.get("time", [])
                temps = hourly.get("temperature_2m", [])

                for i in range(len(times)):
                    record = {
                        "city": city["name"],
                        "time": times[i] if i < len(times) else None,
                        "temperature": temps[i] if i < len(temps) else None,
                        "latitude": data.get("latitude"),
                        "longitude": data.get("longitude"),
                        "timezone": data.get("timezone", "Unknown")
                    }
                    all_records.append(record) # Save data in JSON format

print(f"\nTotal records aggregated: {len(all_records)}")
print(all_records[:5])   # First 5 - should be Tallahassee
print(all_records[360:365])  # Should be Miami
print(all_records[720:725])  # Should be Orlando
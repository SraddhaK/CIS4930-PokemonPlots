# CIS4930-Data Pipeline
The Team: Sam Miller (SSM23A) section 4.4, Sofie Szlezak (SSS23J) section 4.5, Aiden Duncan (AJD24C) section 4.3, Sraddha Karthik (SK23BJ) section 4.1 and 4.2

# Overview
This project seeks to automate making various robust API calls to gather weather data about various Florida cities. It then stores the results for analysis and historical tracking. API used is open-meteo, an open source API for weather tracking. 

# Open-Meteo: https://open-meteo.com/

# Data pipeline goals
  - Fetch hourly temperatures for 3 major Florida cities once per run
  - Accumualte results over time in a CSV and SQLite files to store data
  - Handle errors in making requests and logging these errors in a referencable log file

# Relevancy

The Open-Medeo API is relevent as our project requires timely, location specific weather data for major Florida cities, and is efficient in gathering this data regularly. Moreover, the API is open source and free to use. It allows us various points of data such as temperature, wind speed, percipitation, etc. 

# Open-Medeo Constraints

Open-Medeo requires no API key, as it is open source and pubic. However, it does rate limit requests to 10,000 calls per day limiting the amount of requests we can make for cities. Moreover, the data gathered is not real-time data but rather hourly data ranging from a time lag of 1-4 hours of most recent data. 

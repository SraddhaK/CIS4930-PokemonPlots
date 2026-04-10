# CIS4930-WeatherAPI (Work in Progress)
The Team: Sam Miller (SSM23A) section 4.4, Sofie Szlezak (SSS23J) section 4.5, Aiden Duncan (AJD24C) section 4.3, Sraddha Karthik (SK23BJ) section 4.1 and 4.2

This project seeks to automate making various robust API calls to gather weather data about various Florida cities. It then stores the results for analysis and historical tracking. API used is open-meteo, an open source API for weather tracking. 

Open-Meteo: https://open-meteo.com/

Data pipeline goals: 
  - Fetch hourly temperatures for 3 major Florida cities once per run
  - Accumualte results over time in a CSV and SQLite files to store data
  - Handle errors in making requests and logging these errors in a referencable log file



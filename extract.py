import requests
import pandas as pd

def extract_weather():
    # Define api endpoint
    url = "https://api.openweathermap.org/data/2.5/weather?lat=-1.2921&lon=36.8219&appid=c84569ede6e5f4688e4e8fc032ab4e6f"

    # Access the API and check response
    raw_data = requests.get(url)

    # Convert data to json
    stg_data = raw_data.json()

    # Flatten JSON data into a dataframe
    # The data returned containes mixed series i.e dictionaries and lists
    data = pd.json_normalize(stg_data)

    return data, stg_data # Both are required for transformation
    

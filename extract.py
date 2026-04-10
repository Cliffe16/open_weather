import requests
import pandas as pd

# Define api endpoint
url = "https://api.openweathermap.org/data/2.5/weather?lat=-1.2921&lon=36.8219&appid=c84569ede6e5f4688e4e8fc032ab4e6f"

# Acess the API and check response
raw_data = requests.get(url)
print("Response status code:\n")
print(raw_data, "\n")

# Convert data to json
print("JSON Data:\n") 
stg_data = raw_data.json()
print(stg_data, "\n")

# Flatten JSON data into a dataframe
# The data returned containes mixed series i.e dictionaries and lists
print("Dataframe:\n")
data = pd.json_normalize(stg_data)
print(data)

print(f"Data of type: {type(data)} successfully extracted!")

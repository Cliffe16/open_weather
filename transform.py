import pandas as pd
from extract import extract_weather, data 

def transform_weather():
    # To explicity flatten the nested weather column, use record_path
    data_weather = pd.json_normalize(stg, record_path=['weather']) # Pass stage the json data as list/dictionary is expected, not dataframe(TypeError would be returned)
    
    # Join the data 
    data = data.join(data_weather.add_prefix('weather_')) # The new columns are renamed by adding a prefix(weather_) to avoid the Value Error 

    # Drop the messy column
    data = data.drop(columns=['weather'])

    return data

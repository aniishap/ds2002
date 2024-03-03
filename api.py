#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:09:34 2024

@author: Anisha
"""

import requests
import pandas as pd
import json
import os

def fetch_country_info(url, country_name, response_type):
    try:
        response = requests.get(url.format(country_name))
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred: " + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred: " + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred: " + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred: " + repr(err)
    
    if response_type == 'json':
        result = json.dumps(response.json(), sort_keys=True, indent=4)
    elif response_type == 'dataframe':
        result = pd.json_normalize(response.json())
    else:
        result = "An unhandled error has occurred!"
        
    return result

valid_url = "https://restcountries.com/v3.1/name/{}?fullText=true"
# i wanted to specify with exact country full name
country_name = input("Enter a country name: ")  # user input : country name
response_type = 'json'  

json_string = fetch_country_info(valid_url, country_name, response_type)

response_type='dataframe'
df = fetch_country_info(valid_url, country_name, response_type)
#if isinstance(df, str):
    #print(df)  
#else:
    #print(df.shape)
    #print(df.columns)
    #df.info()
    

def get_api_data(url, country_name, response_type):
    try:
        response = requests.get(url.format(country_name))
        response.raise_for_status()
    
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred: " + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred: " + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred: " + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred: " + repr(err)
        
    return response.json()

json_data = get_api_data(valid_url, country_name, response_type)

capital = json_data[0]['capital'][0]  # extract country's capital
population = json_data[0]['population']  # extract country's population

df = pd.DataFrame({'Capital': [capital], 'Population': [population]})

# write to json file 

def display_country_info(df):
    print("Country Information:")
    print(df)

def write_to_json(df, file_name):
    if os.path.exists(file_name):
        with open(file_name, 'a') as file:
            df.to_json(file, orient='records', lines=True)
    else:
        df.to_json(file_name, orient='records', lines=True)
        

display_country_info(df)

file_name = 'country_information.json'
write_to_json(df, file_name)
print(f"Data stored in {file_name}")







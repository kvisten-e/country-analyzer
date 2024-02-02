import pandas as pd
import wbgapi as wb
import json
import datetime


def save_data_inflation(data):
  data_json = open_json()

  try:  
    inflation_data_to_json = {
      "last_updated": str(datetime.date.today()),
      "countries": data
    }
  except:
    print("Failed..")
    
  data_json['inflation'].update(inflation_data_to_json)
  updated_json = json.dumps(data_json, indent=2)

  save_to_json(updated_json)
    

def save_data_gdp(data):
  data_json = open_json()

    
  try:  
    gdp_data_to_json = {
      "last_updated": str(datetime.date.today()),
      "countries": data
    }
  except:
    print("Failed..")
    
  data_json['GDP'].update(gdp_data_to_json)
  updated_json = json.dumps(data_json, indent=2)

  save_to_json(updated_json)


def save_interest_rate_gdp(data):
  data_json = open_json()
    
  try:  
    interest_rate_data_to_json = {
      "last_updated": str(datetime.date.today()),
      "countries": data
    }
  except:
    print("Failed..")
    
  data_json['interest_rate'].update(interest_rate_data_to_json)
  updated_json = json.dumps(data_json, indent=2)

  save_to_json(updated_json)

def open_json():
    with open('api/data.json', 'r') as file:
      data_json = json.load(file)
    return data_json
  
def save_to_json(updated_json):
    with open('api/data.json', 'w') as file:
      file.write(updated_json)
import json
import datetime

# Denna funktion sparar inflationsdata till JSON-filen
def save_data_inflation(data):
  #Kalalr på funktionen open_json(). Den Retunerar data från JSON-filen
  data_json = open_json()
  
  # Uppdarerar till dagens datum och lägger in nya datan. Skulle något gå fel så kommer inte det nya datumet att eller datan att läggas in 
  inflation_data_to_json = {
    "last_updated": str(datetime.date.today()),
    "countries": data
  }
  #Den nya datan ifrån "inflation_data_to_json" uppdaterar och ersätter den tidigare datan under 'inflation' i JSON-datan
  data_json['inflation'].update(inflation_data_to_json)
  #json.dumps konverterar min "data_json" objekt till JSON-format med en indentering på 2
  updated_json = json.dumps(data_json, indent=2)

  #Kallar på funktionen "save_to_json" och skickar in den konverterade JSON-datan 
  save_to_json(updated_json)

def save_data_gdp(data):
  data_json = open_json()

  gdp_data_to_json = {
    "last_updated": str(datetime.date.today()),
    "countries": data
  }
    
  data_json['GDP'].update(gdp_data_to_json)
  updated_json = json.dumps(data_json, indent=2)

  save_to_json(updated_json)

def save_interest_rate_gdp(data):
  data_json = open_json()

  interest_rate_data_to_json = {
    "last_updated": str(datetime.date.today()),
    "countries": data
  }

  data_json['interest_rate'].update(interest_rate_data_to_json)
  updated_json = json.dumps(data_json, indent=2)

  save_to_json(updated_json)

# Denan funktion öppnar data.json och hämtar ut datan
def open_json():
  #Öppnar upp JSON-filen och sparar i en variabel som senare retuneras. 
  with open('api/data.json', 'r') as file:
    data_json = json.load(file)
  return data_json
#Denna funktion sparar JSON-formenterad data till data.json
def save_to_json(updated_json):
    with open('api/data.json', 'w') as file:
      file.write(updated_json)
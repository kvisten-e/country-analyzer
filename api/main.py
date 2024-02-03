from .fetch_data import inflation_data, gdp_data, interest_rate_data
import pandas as pd

# Startar processen med att hämta ny data 
def get_data():
  print("Loading new data, please wait..")
  # Läser in alla resultat från varje funktion, dessa funktioner hämtar ny data inom varje ämne
  all_result = [inflation_data(), gdp_data(), interest_rate_data()]
  #Loppar igeom varje resultat
  for each_result in all_result:
    #Om något resultat har status "False" så har inte ny data kunnat hämtas från APIn
    if each_result['status'] == False:
      #Då vill jag meddela det och visa när den senaste datan är daterad till (hämtas ifrån JSON-filen)
      print(f"{each_result['message']} - Last updated data: {each_result['last_updated']}")
  
  return True
  
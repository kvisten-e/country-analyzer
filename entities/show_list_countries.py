import pandas as pd

class list_countries:
  def __init__(self):
    pass
  
  def get_all_countries():
    print("")
    csv_data = pd.read_csv("country_codes/country_codes.csv")
    data = pd.DataFrame(csv_data)
    country_list = data['code'] + " | " + data['Country']
    for country in country_list:
      print(country)
    
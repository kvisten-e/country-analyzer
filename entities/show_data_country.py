import pandas as pd
from pandas import json_normalize
import json
import datetime

grab_json_data = pd.read_json("api/data.json")
df = pd.DataFrame(grab_json_data)


def print_country_data(country_code):
  for each_data in df:
    print(each_data)
    country_data_df = df[each_data]['countries'][country_code]
  
    data_df = {
      'År': list(map(int, country_data_df.keys())),
      'Värde': list(country_data_df.values())
    }
    
    data_df = pd.DataFrame(data_df)
    data_df = data_df.sort_values(by='År')
    data_df['Förändring % året innan'] = round(data_df['Värde'].pct_change() * 100,1)
    data_df['Förändring % året innan'] = data_df['Förändring % året innan'].apply(lambda x: f"{x}%")
    data_df['År'] = data_df['År'].apply(lambda x: f" est. {x}" if int(x) > datetime.datetime.now().year else x)
    no_index = data_df.to_string(index=False)
    print(no_index, "\n")

    
def compare_countries(country_code, compare_country_code):
  for each_data in df:
    print(each_data)
    country_data_1 = df[each_data]['countries'][country_code]
    country_data_2 = df[each_data]['countries'][compare_country_code]
    
    data_df = {
      'År': list(map(int, country_data_1.keys())),
      country_code: list(country_data_1.values()),
      compare_country_code: list(country_data_2.values())
    }

    data_df = pd.DataFrame(data_df)
    data_df = data_df.sort_values(by='År')
    data_df['Skillnad %'] = round(data_df[country_code] / data_df[compare_country_code]-1,2)
    data_df['Skillnad %'] = data_df['Skillnad %'].apply(lambda x: f"{x}%")
    data_df['År'] = data_df['År'].apply(lambda x: f" est. {x}" if int(x) > datetime.datetime.now().year else x)
    no_index = data_df.to_string(index=False)
    print(no_index, "\n")
    
def get_country_data(country_code):
  for each_data in df:
    print(each_data)
    country_data_df = df[each_data]['countries'][country_code]
  
    data_df = {
      'År': list(map(int, country_data_df.keys())),
      'Värde': list(country_data_df.values())
    }
    
    data_df = pd.DataFrame(data_df)
    data_df = data_df.sort_values(by='År')
    data_df['Förändring % året innan'] = round(data_df['Värde'].pct_change() * 100,1)
    data_df['Förändring % året innan'] = data_df['Förändring % året innan'].apply(lambda x: f"{x}%")
    data_df['År'] = data_df['År'].apply(lambda x: f" est. {x}" if int(x) > datetime.datetime.now().year else x)
    no_index = data_df.to_string(index=False)
    print(no_index, "\n")
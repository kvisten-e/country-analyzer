import pandas as pd
from pandas import json_normalize
import json
import datetime

grab_json_data = pd.read_json("api/data.json")
df = pd.DataFrame(grab_json_data)

class data_countries:
  def __init__(self):
    pass

  def get_country_data(country_code):
    #country_data_df = [df['inflation']['countries'][country_code], 
    #                  df['GDP']['countries'][country_code], 
    #                  df['interest_rate']['countries'][country_code]]
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
      
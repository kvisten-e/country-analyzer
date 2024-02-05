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
    print(f"\n{each_data}")
    country_data_1 = df[each_data]['countries'][country_code]
    country_data_2 = df[each_data]['countries'][compare_country_code]    
    
    if each_data == "GDP":
      
      country_code_text = f"{country_code} ($ billions)"
      compare_country_code_text = f"{compare_country_code} ($ billions)"
      
      data_df = {
        'Year': list(map(int, country_data_1.keys())),
        country_code_text: list(country_data_1.values()),
        compare_country_code_text: list(country_data_2.values())
      }
      data_df = pd.DataFrame(data_df)
      data_df = data_df.sort_values(by='Year')
      try:
        data_df[country_code_text] = data_df[country_code_text].apply(lambda x: round(x/1000000000))
        data_df[compare_country_code_text] = data_df[compare_country_code_text].apply(lambda x: round(x/1000000000))
        data_df['Difference in %'] = round((data_df[country_code_text] / data_df[compare_country_code_text]-1)*100,1)
        data_df['Difference in %'] = data_df['Difference in %'].apply(lambda x: f"{x}%")
        data_df['Year'] = data_df['Year'].apply(lambda x: f" est. {x}" if int(x) > datetime.datetime.now().year else x)
        no_index = data_df.to_string(index=False)
        print(no_index)
      except Exception as e:
        print(e)

    else:   
      data_df = {
        'Year': list(map(int, country_data_1.keys())),
        country_code: list(country_data_1.values()),
        compare_country_code: list(country_data_2.values())
      }

      data_df = pd.DataFrame(data_df)
      data_df = data_df.sort_values(by='Year')
      data_df['Difference in %'] = round((data_df[country_code] / data_df[compare_country_code]-1)*100,1)
      data_df['Difference in %'] = data_df['Difference in %'].apply(lambda x: f"{x}%")
      data_df['Year'] = data_df['Year'].apply(lambda x: f" est. {x}" if int(x) > datetime.datetime.now().year else x)
      no_index = data_df.to_string(index=False)
      print(no_index, "\n")
    
def get_country_data(country_code):
  data_total = []
  for each_data in df:
    country_data_df = df[each_data]['countries'][country_code]
  
    data_df = {
      'type': each_data, 
      'year': list(map(int, country_data_df.keys())),
      'value': list(country_data_df.values())
    }
    
    data_total.append(data_df)

  return data_total
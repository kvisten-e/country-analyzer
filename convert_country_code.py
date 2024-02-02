import pandas as pd

class country_code():
  def __init__(self):
    pass
  
  def single_country_code(code):
    #Läs in data från csv-fil och gör en Dataframe class av det med hjälp av pandas
    df = pd.read_csv('country_codes.csv')
    
    #Kolla om något värde i df['code'] har detsamma som 'code' variablen, om så är fallet, så plockar any() funktionen upp det True värdet
    if any(df['code'] == code):
      
      # Använder .loc[] funktionen för att leta reda på vilken index som retunerat True sedan tidigare och väljer att plocka upp värdet under labeln 'Country'
      # iloc plockar ut bara värdet ur objektet som skapas
      return df.loc[df['code'] == code, 'Country'].iloc[0]
  
  print(single_country_code("SWE"))
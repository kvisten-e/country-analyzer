import pandas as pd
import country_codes.convert_country_code as cc
import numpy as np

class countries_data():

  data = pd.read_json('api/data.json')
  df = pd.DataFrame(data)
  
  def list_countries(self, type):
    #Skriver ut vilken typ av data som ska presenteras
    print(f"\n{type}")
    
    #Kallar på funktionen som skapar ny dict med alla länders data
    country_dict = self.create_dataframe(type)
    
    # Gör en Dataframe av våran nya dict.
    data_df = pd.DataFrame(country_dict)
    #Sortera listan efter ländernas namn
    data_df = data_df.sort_values(by='Country')
    
    #Plockar bort index värdet för varje rad
    data_df_no_index = data_df.to_string(index=False)
    print(data_df_no_index)


  def list_countries_gdp(self):
    print(f"\nGDP ($ Billions)")
    
    country_dict = self.create_dataframe('GDP')
    
    data_df = pd.DataFrame(country_dict)
    data_df = data_df.sort_values(by='Country')
    # Jag använder iloc för att plocka ut de rader och kolumner ([rad_start:rad_slut, kolumn_start:kolumn_slut]) jag vill manipullera. Därefter går jag igenom varje rads värde och dividerar
    # Pågrund av divisionen så konverteras x till ett float64, vart tvungen att göra en .round() för att bli av med decimalerna och sedan en .astype() för att göra den till en int64 igen
    data_df.iloc[:, 1:] = data_df.iloc[:, 1:].apply(lambda x: (x/1000000000).round().astype('int64'))
    data_df_no_index = data_df.to_string(index=False)
    print(data_df_no_index)      
    
    
    
    
    
  def create_dataframe(self, type):
    #Plockar ut enbart datan från JSON-filen på datan som ska presenteras
    values_df = self.df[type]['countries']
    
    #Skapar en ny dict som senare ska bli den nya dataframen. Jag lägger till alla nycklar (landskod ifrån JSON) som en lista 
    country_dict = {
      'Country': list(values_df.keys())
    }
    # Loopar igenom varje lands dicts
    for each_country in values_df.values():
      # Loopar igenom varje lands dict och plockar ut dess key och values
      for year, value in each_country.items():
        # Kollar om året är tillagd som 'key' i details dicten. Finns den redan med, lägg till landets värde för det året i listan
        if year in country_dict:
          country_dict[year].append(value)
        # Finns året inte med, skapa 'key' och lägg till första värdet i en lista
        else:
          country_dict[year] = [value]
    
    return country_dict
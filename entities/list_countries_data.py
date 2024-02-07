import pandas as pd
import country_codes.convert_country_code as cc
import numpy as np

class countries_data():

  data = pd.read_json('api/data.json')
  df = pd.DataFrame(data)
  
  # Skriver ut alla länders data beroende på typ (Inflation eller ränta)
  def list_countries(self, type):
    #Skriver ut vilken typ av data som ska presenteras
    print(f"\n{type}")
    
    #Kallar på funktionen som skapar ny dict med alla länders data
    country_dict = self.get_data_for_dataframe(type)
    result = self.get_higest_lowest(country_dict)
    
    # Gör en Dataframe av våran nya dict.
    data_df = pd.DataFrame(country_dict)
    #Sortera listan efter ländernas namn
    data_df = data_df.sort_values(by='Country')
    
    #Plockar bort index värdet för varje rad
    data_df_no_index = data_df.to_string(index=False)
    print(data_df_no_index, "\n")
    
    first_print = True
    for result_dict in result:
      for country, value in result_dict.items():
        if first_print:
          print(f"{country} have the highest {type}: {round(value,1)}")
          first_print = False
        else:
          print(f"{country} have the lowest {type}: {round(value,1)}")
  
  
  # Skriver ut alla länders GDP data
  def list_countries_gdp(self):
    print(f"\nGDP ($ Billions)")
    
    country_dict = self.get_data_for_dataframe('GDP')
    result = self.get_higest_lowest(country_dict)
    
    
    data_df = pd.DataFrame(country_dict)
    data_df = data_df.sort_values(by='Country')
    # Jag använder iloc för att plocka ut de rader och kolumner ([rad_start:rad_slut, kolumn_start:kolumn_slut]) jag vill manipullera. Därefter går jag igenom varje rads värde och dividerar
    # Pågrund av divisionen så konverteras x till ett float64, vart tvungen att göra en .round() för att bli av med decimalerna och sedan en .astype() för att göra den till en int64 igen
    data_df.iloc[:, 1:] = data_df.iloc[:, 1:].apply(lambda x: (x/1000000000).round().astype('int64'))
    data_df_no_index = data_df.to_string(index=False)
    print(data_df_no_index, "\n")      
    
    first_print = True    
    for result_dict in result:
      for country, value in result_dict.items():
        if first_print:
          print(f"{country} have the highest GDP: {round(value / 1000000000)}")
          first_print = False
        else:
          print(f"{country} have the lowest GDP: {round(value / 1000000000)}")

  # Tar fram det högsta och lägsta värdet för det senaste året från 
  def get_higest_lowest(self, data):
    #Hämta in datan och konvertera till en Dataframe
    df = pd.DataFrame(data)
    #Jag plockar ut det senaste året som finns i datan. Jag plockar "kolumn raden" med [1:1] och gör det till en lista med värdena, sen så plockar jag det andra värdet i listan vilket är det senaste året
    year = list(df[1:1])[1]

    # Jag hämtar index för maxvärdet i kolumn year (2022)
    index_max_value_latest = df[year].idxmax()
    #Hämtar ut landets kod med samma index
    country_max_value_latest = df.loc[index_max_value_latest, 'Country']
    # Konverterar landets code (SWE) till Sweden
    country_name_max = cc.single_country_code(country_max_value_latest)
    #Hämtar ut värdet för index
    value_max_value_latest = df.loc[index_max_value_latest, year]
    
    index_min_value_latest = df[year].idxmin()
    country_min_value_latest = df.loc[index_min_value_latest, 'Country']
    country_name_min = cc.single_country_code(country_min_value_latest)
    value_min_value_latest = df.loc[index_min_value_latest, year]
    
    
    return[{country_name_max: value_max_value_latest}, {country_name_min: value_min_value_latest}]
  
  #Här hämtas och konverteras type (gdp, inflation, interest_rate) data och retuneras. 
  def get_data_for_dataframe(self, type):
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
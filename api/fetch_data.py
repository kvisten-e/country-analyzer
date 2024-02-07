import wbgapi as wb
import datetime
from .save_data import save_data_inflation, save_data_gdp, save_interest_rate_gdp
import urllib, json
from country_codes.convert_country_code import list_country_codes

# Hämtar in en lista på alla länder koder (SWE,DDK,DEU..)
european_countries = list_country_codes()

# Skapar ett en lista med start och slut år för data som ska presenteras. 
def years_for_data():  
  return [datetime.datetime.now().year-6, datetime.datetime.now().year]
year = years_for_data()

# Hämtar inflationsdata ifrån biblioteket wbgapi (World Bank's data API)
def inflation_data():
  # Skapar en tom dict. Denna ska innehålla varje land med tillhörande data för varje år
  inflation_data_api = {}
  try:
    # Hämtar in data. "FP.CPI.TOTL.ZG" = vilken typ av data som ska hämtas från databasen. Resten är vilka länder och mellan vilka år som datan ska innehålla
    data = wb.data.fetch('FP.CPI.TOTL.ZG', european_countries, range(year[0], year[1]))
    #Gör en loop för varje resultat (Varje land med data för varje år)
    for row in data:
      # Kollar om landet inte redan finns i "inflation_data_api" som nyckel, om så är fallet, lägg till datan ({'SWE':{år:värde}})
      if row['economy'] not in inflation_data_api.keys():
        inflation_data_api[row['economy']] = {int(row['time'][2:]): round(row['value'],2)}
      # Skulle landet redan finnas med, fyll då på med värde för det året som loppas.
      else:
        inflation_data_api[row['economy']][int(row['time'][2:])] = round(row['value'],2)
  #Skulle APIn ligga nere eller få Timeout så kommer detta meddelande att retuneras. "Status" kommer senare bestämma om meddelandet ska skrivas ut. "last_updated" hämtar när datan senast hämtades 
  except Exception as e:
    return {"message": 'Failed to fetch new inflation data', "status": False, "last_updated": get_last_updated_date('inflation')}

  #Denna kod sparar den hämtade datan till min JSON-fil
  try:  
    save_data_inflation(inflation_data_api)
  except:
    return {"message": 'Failed to save new inflation data to json', "status": False, "last_updated": get_last_updated_date('inflation')}

  return {"message": "Success", "status": True, "last_updated": get_last_updated_date('inflation')}

def gdp_data():
  message = ''
  gdp_data_api = {}
  try:
    data = wb.data.fetch('NY.GDP.MKTP.KD', european_countries, range(year[0], year[1]))
    for row in data:
      if row['economy'] not in gdp_data_api.keys():
        gdp_data_api[row['economy']] = {int(row['time'][2:]): round(row['value'])}
      else:
        gdp_data_api[row['economy']][int(row['time'][2:])] = round(row['value'])
      
  except Exception as e:
    return {"message": 'Failed to fetch new gdp data' , "status": False, "last_updated": get_last_updated_date('GDP')}
  try:  
    save_data_gdp(gdp_data_api)
  except:
    return {"message": 'Failed to save new gdp data to json' , "status": False, "last_updated": get_last_updated_date('GDP')}
   
  return {"message": "Success", "status": True, "last_updated": get_last_updated_date('GDP')}

def interest_rate_data():
  message = ''
  interest_data_api = {}
  api_inflation_rate_url = "https://www.imf.org/external/datamapper/api/v1/PCPIPCH"

  try:
    # Använder mig här av urllib för att hämta hem datan från APIn i JSON format
    with urllib.request.urlopen(api_inflation_rate_url) as response:
      body_json = response.read()
    # Tilldelar JSON filen till variablen data, där jag blandanat sorterat ut 'values' och 'PCPIPCH' från json datan då det inte är tillanvänding för mig
    data = json.loads(body_json)['values']['PCPIPCH']

    # Jag gör en loop genom alla länder jag valt att ha med för att hämta ut json datan just för det landet
    for country in european_countries:
      #Skapar en tom 'dict' för att bara spara data inom ett visst årsspann för varje land.
      trim_values = {}
      # Jag kollar om landets förkortning ifrån "european_countries" finns med i JSON filen.
      if country in data:
        # Tilldelar just det landets data till en variabel
        country_inflation_data = data[country]
      
        # Denna loop plockar ut data inom ett visst årsspann och placerar i den tidigare deklarerade variablen "trim_values"
        for year_str, rate in country_inflation_data.items():
          # Formaterar om året ifrån JSON filen till typen int
          year_row = int(year_str)
          # Plockar bara ut den data som är inom årsspannet, så sparar bara datan där 'year_row' blir True
          if year_row > year[1]-7 and year_row < year[1]-1:
            # Lägger in datan i 'trim_values
            trim_values[year_str] = rate
            # Då datan som hämtas från IMF har en annan riktning sett till wbgapi så måste jag göra en reverse på den.
            # Jag plockar keys och values ifrån trim_values och lägger dem i en lista, jag gör en reverse på listan och formenterar om listan till en dict igen. 
            trim_values = dict(reversed(list(trim_values.items())))
            
      # Här skapar jag en ny dict med landets förkortning och en dict med year: rate datan. Den läggs då till i "interest_data_api"
      interest_data_api[country] = trim_values
      
  except Exception as e:
    return {"message": 'Failed to fetch new interest rate data'  , "status": False , "last_updated": get_last_updated_date('interest_rate')}
  try:  
    save_interest_rate_gdp(interest_data_api)
  except:
    return {"message": 'Failed to save new intrerest data to json'  , "status": False , "last_updated": get_last_updated_date('interest_rate')}
    
  return {"message": "Success", "status": True, "last_updated": get_last_updated_date('interest_rate')}



# Denna funktionen retunerar vilket datum ifrån JSON file som en dict senast blivit uppdaterad. Type är om det är inflations- dgb eller räntedata 
def get_last_updated_date(type):
  with open('api/data.json', 'r') as file:
    data_json = json.load(file)
    return data_json[type]['last_updated']


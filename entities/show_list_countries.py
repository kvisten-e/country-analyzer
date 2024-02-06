import pandas as pd

# Denna funktion skriver ut en lista på alla länder som finns i csv filen (Samma länder som kallas och har data i JSON-filen)
def get_all_countries():
  print("")
  #Läser in csv-filen mef hjälp av pandas och sparar datan i en variabel
  csv_data = pd.read_csv("country_codes/country_codes.csv")
  #Konverterar datan till en Dataframe
  data = pd.DataFrame(csv_data)
  
  #Tar data från varje rad och slår ihop landets kod och namn
  country_list = data['code'] + " | " + data['Country']
  # Gör en loop för varje rad i den nya skapade lista och skriver ut värdet. (EST | Estonia)
  for country in country_list:
    print(country)
    
  return data

import pandas as pd
import datetime

df = pd.read_json("api/data.json")

# Skriver ut en enskillds lands data
def print_country_data(country_code):
  # Loopar igenom de tre indikatorerna (inflation, gdp, interest_rate)
  for each_data in df:
    print(f"\n{each_data}")
    #Plockar ut ett lands data för indikatiorn. Det innehåller då år och värde
    country_data_df = df[each_data]['countries'][country_code]

    # Om de är GDP så vill jag skriva ut mer text så därav har den en egen if.
    if each_data == "GDP":
      each_data_text = f"{each_data} ($ billions)"
      #Skapar en ny dict och lägger in värdena som hämtats
      data_df = {
        'Year': list(map(int, country_data_df.keys())),
        each_data_text: list(country_data_df.values())
      }      
      
      #Formenterar om dicten till en Dataframe
      data_df = pd.DataFrame(data_df)
      #Sorterar den på keyn 'year'
      data_df = data_df.sort_values(by='Year')
      #Går igenom alla värden under keyn 'each_data_text' och skalar ner dess värde för att lättare kunnas presenteras i terminalen
      data_df[each_data_text] = data_df[each_data_text].apply(lambda x: round(x/1000000000))
      #Skapar här en ny kolumn (key) där jag använder mig av pandas metod .pct_change(). Den ser till att jämnföra procentskillnaden med värdet från raden innan
      data_df['Change % from the previous year'] = round(data_df[each_data_text].pct_change() * 100,1)
      # Jag lägger här till text till den uträknade procentsiffran med ett %-tecken. Jag tar även bort värdet för 2018 då den inte har ett årtal tidigare att jämföras med (pd.notna kollar om x är nan, om så är fallet, gör den tom)
      data_df['Change % from the previous year'] = data_df['Change % from the previous year'].apply(lambda x: f"{x}%" if pd.notna(x) else "")
      #Tar bort index värdena för varje rad då det inte är relevenat för användaren
      no_index = data_df.to_string(index=False)
      print(no_index)      
      
    else:
      #Denna else tar hand om inflation/interest_rate
      data_df = {
        'Year': list(map(int, country_data_df.keys())),
        each_data: list(country_data_df.values())
      }
      
      data_df = pd.DataFrame(data_df)
      data_df = data_df.sort_values(by='Year')
      data_df['Change % from the previous year'] = round(data_df[each_data].pct_change() * 100, 1)
      data_df['Change % from the previous year'] = data_df['Change % from the previous year'].apply(lambda x: f"{x}%" if pd.notna(x) else "")
      no_index = data_df.to_string(index=False)
      print(no_index)

# Jämnför data mellan två länder
# Kod likt tidigare upplägg
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
      print(no_index)
      
# Denna funktion används för att hämta ett en enskillds lands data och retunera den
def get_country_data(country_code):
  data_total = []
  # Loopar igenom varje dict från data.json. ('inflation', 'gdp', 'interest_rate')
  for each_data in df:
    #Plockar ur values från ett land(key). Så alla år och dess värde
    country_data_df = df[each_data]['countries'][country_code]
    #Skapar en ny dict och strukturerar om datan som sen ska sparas i den nya listan "data_total"
    #Jag tar åren som hämtas och lägger dem i en lista. Gör samma process för värdena. 
    #each_data är vilken typ av data det är (inflation)
    data_df = {
      'type': each_data, 
      'year': list(map(int, country_data_df.keys())),
      'value': list(country_data_df.values())
    }
    #Lägger till den nyskapade dicten i listan
    data_total.append(data_df)
  #Retunerar ett lands totala data
  return data_total
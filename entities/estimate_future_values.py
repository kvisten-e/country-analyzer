import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from .show_data_country import *

# Denna funktion skapar ett estimerat resultat med hjälp av Linjär regression
def estimate_future(year, code):
  # Hämta in ett lands data
  data_total = get_country_data(code)

  # Loppar igeom varje data typ
  for each_type in data_total:
    match each_type['type']:
      case 'inflation':
        print("\nInflation estimated based on Linear Regression")  
        # Skapar en ny dict och tilldelar data som tidigare hämtas med funktion "get_country_data" och plockar ut varje värde inder 'year', 'type' och 'value'
        data = {
          'Year': each_type['year'],
          each_type['type']: each_type['value']
        }

        df = pd.DataFrame(data)

        # Data omformas för att formatet ska passa biblioteket "sklearn.linear_model"
        x = df['Year'].values.reshape(-1, 1) 
        y = df[each_type['type']].values

        # En modell skapas och tränas för att se sammanhanget mellan x och y. För att senare kunna ta fram ett värde baserat på vilket år den blir tilldelad
        model = LinearRegression()
        model.fit(x, y)

        # Ta fram vilket år som modellen ska estimera fram ett värde på. Year formateras om med hjälp av Numpy för att passa inmatning till model.predict.
        forecast_year = np.array([[year]])
        # Ett esitmerat värde tas fram med hjälp av .predict() ifrån "LinearRegression"
        predicted_inflation = model.predict(forecast_year)
        # Värdet rundas av med två decimaler.
        predicted_inflation = round(predicted_inflation[0],2)
        # Loc tillåter mig att lägga till nytt värde i min dataframe baserat på vilket index jag väljer att det nya värdet ska hamna på
        df.loc[len(df)] = [year, predicted_inflation]
        
        #Sortera listan efter key 'year'
        df = df.sort_values(by='Year')
        
        #Loopar igenom varje värde under key [each_type['type]] och avrundar dess värde med två decimaler
        df[each_type['type']] = df[each_type['type']].apply(lambda x: f"{round(x,2)}%")
        #Kollar om något value under keyn 'Year' är större än detta året, om så är fallet, läggs est. i början av texten
        df['Year'] = df['Year'].apply(lambda x: f" est. {int(x)}" if int(x) > datetime.datetime.now().year else int(x))  
        # Index värdet för varje rad tas bort.       
        no_index = df.to_string(index=False)
        print(no_index)
        
      case 'GDP':
        print("\nGDP estimated based on Linear Regression")  
        gdp_text = f"{each_type['type']} (billions)"
        data = {
          'Year': each_type['year'],
          gdp_text: each_type['value']
        }
        
        df = pd.DataFrame(data)

        x = df['Year'].values.reshape(-1, 1)  
        y = df[gdp_text].values

        model = LinearRegression()
        model.fit(x, y)

        forecast_year = np.array([[year]])
        predicted_inflation = model.predict(forecast_year)
        predicted_inflation = round(predicted_inflation[0],2)

        df.loc[len(df)] = [year, predicted_inflation]
        df = df.sort_values(by='Year')
        df[gdp_text] = df[gdp_text].apply(lambda x: f"{round(x/1000000000)}")
        df['Year'] = df['Year'].apply(lambda x: f" est. {int(x)}" if int(x) > datetime.datetime.now().year else int(x))        
        no_index = df.to_string(index=False)
        print(no_index, "\n")
        
      case 'interest_rate': 
        print("\nInterest rate estimated based on Linear Regression")  
        interest_rate_text = f"{each_type['type']}"
        data = {
          'Year': each_type['year'],
          interest_rate_text: each_type['value']
        }
        df = pd.DataFrame(data)
        
        x = df['Year'].values.reshape(-1, 1)  
        y = df[interest_rate_text].values  

        model = LinearRegression()
        model.fit(x, y)

        forecast_year = np.array([[year]])
        predicted_inflation = model.predict(forecast_year)
        predicted_inflation = round(predicted_inflation[0],2)

        df.loc[len(df)] = [year, predicted_inflation]
        df = df.sort_values(by='Year')
        df[interest_rate_text] = df[interest_rate_text].apply(lambda x: f"{round(x,2)}%")
        df['Year'] = df['Year'].apply(lambda x: f" est. {int(x)}" if int(x) > datetime.datetime.now().year else int(x))        
        no_index = df.to_string(index=False)
        print(no_index, "\n")


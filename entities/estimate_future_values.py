import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from .show_data_country import *

def estimate_future(year, code):
  data_total = get_country_data(code)

  for each_type in data_total:
    match each_type['type']:
      case 'inflation':
        print("\nInflation estimated based on Linear Regression")  
    
        data = {
          'Year': each_type['year'],
          each_type['type']: each_type['value']
        }
        # Create a DataFrame
        df = pd.DataFrame(data)

        # Reshape the data (scikit-learn expects a 2D array for the independent variables)
        x = df['Year'].values.reshape(-1, 1)  # Independent variable
        y = df[each_type['type']].values  # Dependent variable

        # Create and fit the model
        model = LinearRegression()
        model.fit(x, y)

        # Predict the inflation for year
        forecast_year = np.array([[year]])
        predicted_inflation = model.predict(forecast_year)
        predicted_inflation = round(predicted_inflation[0],2)
        # Loc tillåter mig att lägga till nytt värde i min dataframe baserat på vilket index jag väljer att det nya värdet ska hamna på
        df.loc[len(df)] = [year, predicted_inflation]
        df = df.sort_values(by='Year')
        
        df[each_type['type']] = df[each_type['type']].apply(lambda x: f"{round(x,2)}%")
        df['Year'] = df['Year'].apply(lambda x: f" est. {int(x)}" if int(x) > datetime.datetime.now().year else int(x))        
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
        
        df[interest_rate_text] = df[interest_rate_text].apply(lambda x: f"{round(x,2)}%")
        df['Year'] = df['Year'].apply(lambda x: f" est. {int(x)}" if int(x) > datetime.datetime.now().year else int(x))        
        no_index = df.to_string(index=False)
        print(no_index, "\n")

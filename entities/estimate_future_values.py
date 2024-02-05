import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def estimate_future(year,):
  data = {
      'Year': [2018, 2019, 2020, 2021, 2022],
      'Inflation': [0.49, 0.94, -0.33, 2.36, 7.81]
  }

  # Create a DataFrame
  df = pd.DataFrame(data)

  # Reshape the data (scikit-learn expects a 2D array for the independent variables)
  x = df['Year'].values.reshape(-1, 1)  # Independent variable
  y = df['Inflation'].values  # Dependent variable

  # Create and fit the model
  model = LinearRegression()
  model.fit(x, y)

  # Predict the inflation for 2025
  forecast_year = np.array([[2025]])
  predicted_inflation = model.predict(forecast_year)
  predicted_inflation = round(predicted_inflation[0],2)

  print(f"Forecasted inflation rate for 2025: {predicted_inflation}%")







""" import matplotlib.pyplot as plt

# Continue from the previous example...

# Predict for the range of years in the dataset and the forecast year
X_future = np.array([[year] for year in range(2018, 2026)])  # Up to 2025
y_future = model.predict(X_future)

# Plot the historical data
plt.scatter(df['Year'], df['Inflation'], color='black', label='Historical Data')

# Plot the regression line
plt.plot(X_future, y_future, color='blue', linestyle='-', label='Forecast')

# Highlight the forecasted year
plt.scatter(2025, predicted_inflation, color='red', label='2025 Forecast')

# Adding titles and labels
plt.title('Inflation Forecast')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')
plt.legend()

# Save the plot to a file
plt.savefig('inflation_forecast.png')

# Show the plot
plt.show() """

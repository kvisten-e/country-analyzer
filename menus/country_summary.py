import entities.show_list_countries as sl
import country_codes.convert_country_code as cc
import entities.show_data_country as sdc
import entities.estimate_future_values as ef
import pandas as pd
import datetime

class summary_country:
  # Funktionen låter användaren skriva in vilket land man vill ta fram data
  def choose_country(self):
    #Skriver ut alla länder som man kan välja att hämta data på
    sl.get_all_countries()

    run = True
    while run:
      try:
        print("\n -- Menu: View a country's financial development --")
        answer = input("Choose country (e.g., SWE): ").strip()
        # Kollar att ens val av land finns med i datan. Den stämmer av med en lokalt sparad csv-fil med alla länder tillgängliga
        if self.check_country_code_exist(answer.strip().upper()):
          run = False
          # Översätter landes kod till sitt fulla namn
          print(f"\n{cc.single_country_code(answer.upper())}") 
          # Skriver ut landets data
          sdc.print_country_data(answer.upper())
          #Startar meny för att kunna arbeta vidare med den data som presenterats
          self.menu_summary(answer.upper())
        else:
          print("The country does not exist, try again")
      except Exception as e:
        print("Something went wrong, try again.", e)
    
      
  def menu_summary(self, country_code):
    print("\n1. Compare data with another country"
          "\n2. Create forecast for year X"
          "\n3. Go to start menu")
    
    run = True
    while run:
      answer = input("-> ").strip()
      match answer:
        case "1":
          run = True
          while run:
            answer = input("Choose country (e.g., SWE): ").strip().upper()
            if self.check_country_code_exist(answer):
              # Kollar så att landet man ska jämnföra mot inte är samma som första valet
              if country_code != answer:
                run = False
                # Kallar på fuktioen "compare_countries" som i sin tur printar ut data
                sdc.compare_countries(country_code, answer)
              else:
                print("The countries cannot be the same as each other")  
            else:
              print("The country does not exist, try again")
        case "2":
          choose_year = True
          while choose_year:
            # Låter användaren mata in ett år för att skapa en prognos på
            estimate_year = int(input("Choose a year: "))
            # Året måste vara större än nuvarande år (2024)
            if estimate_year > datetime.datetime.now().year:
              run = False
              choose_year = False
              # Uppfylls kravet så avslutas looparna run & choose_year och funktionen "estimate_future" startas
              ef.estimate_future(estimate_year, country_code)
            else:
              print("Select a year that is greater than the current year.")
        case "3":
          run = False
        case _:
          print("Wrong input, try again")

  # Landets kod (SWE) skickas in och funktionen kollar om landet finns med i csv-filen, om så är fallet så returneras true
  def check_country_code_exist(self, code):
    csv_data = pd.read_csv("country_codes/country_codes.csv")
    data = pd.DataFrame(csv_data)
    # .isin() är en pandas metod som tillåter en att leta i en dataframe efter ett värde. 
    if data.isin([code]).any().any():
      return True
    else:
      return False
    
    
  
  def __init__(self):
    self.choose_country()

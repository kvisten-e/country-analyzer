import entities.show_list_countries as sl
import country_codes.convert_country_code as cc
import entities.show_data_country as sdc
import entities.estimate_future_values as ef
import pandas as pd
import datetime

class summary_country:

  def choose_country(self):
    sl.get_all_countries()

    run = True
    while run:
      try:
        print("\n -- Menu: View a country's financial development --")
        answer = input("Choose country (e.g., SWE): ").strip()
        if self.check_country_code_exist(answer.strip().upper()):
          run = False
          print("\n", cc.single_country_code(answer.upper()), "\n")  
          sdc.print_country_data(answer.upper())    
          self.menu_summary(answer.upper())
        else:
          print("The country does not exist, try again")
      except Exception as e:
        print("Something went wrong, try again.", e)
    
      
  def menu_summary(self, country_code):
    print("\n1. Compare data with another country"
          "\n2. Create forecast for X years"
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
              if country_code != answer:
                run = False
                sdc.compare_countries(country_code, answer)
              else:
                print("The countries cannot be the same as each other")  
            else:
              print("The country does not exist, try again")
        case "2":
          choose_year = True
          while choose_year:
            estimate_year = int(input("Choose a year: "))
            if estimate_year > datetime.datetime.now().year:
              run = False
              choose_year = False
              ef.estimate_future(estimate_year, country_code)
            else:
              print("Choose a year larger than this year")
        case "3":
          run = False
        case _:
          print("Wrong input, try again")
        
  
  def see_all_countries(self):  
    print("test")
    
    
  def check_country_code_exist(self, code):
    csv_data = pd.read_csv("country_codes/country_codes.csv")
    data = pd.DataFrame(csv_data)
    
    if data.isin([code]).any().any():
      return True
    else:
      return False
    
    
  
  def __init__(self):
    self.choose_country()

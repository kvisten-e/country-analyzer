import entities.show_list_countries as sl
import country_codes.convert_country_code as cc
import entities.show_data_country as sdc
import entities.estimate_future_values as ef
import pandas as pd


class summary_country:

  def choose_country(self):
    sl.get_all_countries()

    run = True
    while run:
      try:
        print("\n -- Meny: Se ett lands finansiella utveckling --")
        answer = input("Välj land (ex. SWE): ").strip()
        if self.check_country_code_exist(answer.strip().upper()):
          run = False
          print("\n", cc.single_country_code(answer.upper()), "\n")  
          sdc.print_country_data(answer.upper())    
          self.menu_summary(answer.upper())
        else:
          print("Landet finns inte med, testa igen")
      except Exception as e:
        print("Något gick fel, testa igen.", e)
    
      
  def menu_summary(self, country_code):
    print("\n1. Jämnför data med ett annat land"
          "\n2. Skapa prognos efter x år"
          "\n3. Gå till start meny")
    answer = input("-> ").strip()
    run = True
    while run:
      match answer:
        case "1":
          run = True
          while run:
            answer = input("Välj land (ex. SWE): ").strip().upper()
            if self.check_country_code_exist(answer):
              run = False
              sdc.compare_countries(country_code, answer)
            else:
              print("Landet finns inte med, testa igen")
        case "2":
          estimate_year = int(input("Välj ett år: "))
          ef.estimate_future(estimate_year, country_code)
        case "3":
          run = False
        case _:
          print("Wrong input, try again")
          e = input("hej")
        
  
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
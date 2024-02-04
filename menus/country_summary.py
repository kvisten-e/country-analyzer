from entities.show_list_countries import list_countries
from entities.show_data_country import data_countries
import country_codes.convert_country_code as cc

class summary_country:

  def choose_country(self):
    data = list_countries.get_all_countries()
    print(list)
    run = True
    while run:
      try:
        print("\n -- Meny: Se ett lands finansiella utveckling --")
        answer = input("Välj land (ex. SWE): ").strip()
        
        if data.isin([answer.upper()]).any().any():
          run = False
          print("\n", cc.single_country_code(answer.upper()), "\n")  
          data_countries.get_country_data(answer.upper())    
          self.menu_summary()
        else:
          print("Landet finns inte med, testa igen")
      except:
        print("Något gick fel, testa igen.")
    
      
  def menu_summary(self):
    print("\n1. Jämnför data med ett annat land"
          "\n2. Skapa prognos efter x år"
          "\n3. Gå till start meny")
    answer = input("-> ").strip()
    run = True
    while run:
      match answer:
        case "1":
          print("Something")
        #case "2":
        case "3":
          run = False
        case _:
          print("Wrong input, try again")
        
  
  def see_all_countries(self):  
    print("test")
    
    
  
  def __init__(self):
    self.choose_country()
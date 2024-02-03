from entities.show_list_countries import list_countries
from entities.show_data_country import data_countries

class summary_country:

  def choose_country(self):
    list_countries.get_all_countries()
    print("\n -- Meny: Se ett lands finansiella utveckling --")
    answer = input("Välj land (ex. SWE): ").strip()  
    
    data_countries.get_country_data(answer.upper())
      
  def menu_summary(self):
    print("\n -- Meny: Se ett lands finansiella utveckling --"
          "\n1. Jämnför med ett annat land"
          "\n2. Skapa prognos efter x år"
          "\n3. Gå till start meny")
    answer = input("-> ").strip()
  
  def see_all_countries(self):  
    print("test")
    
    
  
  def __init__(self):
    self.choose_country()
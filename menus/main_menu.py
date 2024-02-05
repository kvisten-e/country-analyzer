from .country_summary import summary_country
import program
from entities.list_countries_data import countries_data

class main_menu:
  def show_main_menu(self):
        run = True
        while run:
          print("\n1. View a country's financial development"
                "\n2. View countries GDP"
                "\n3. View countries Inflation"
                "\n4. View countries Interest rates"
                "\n5. Exit")
          answer = input("-> ").strip()
          
          cd = countries_data()
          match answer:
            case "1":
              summary_country()
            case "2":
              cd.list_countries_gdp()
            case "3":
              cd.list_countries('inflation')
            case "4":
              cd.list_countries('interest_rate')

            case "5":
              run = False
              program.close_program()
            case _:
              print("Wrong input, try again..")

  def __init__(self):
    self.show_main_menu()
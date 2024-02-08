from .country_summary import Summary_country
import program
from entities.list_countries_data import Countries_data

#Skapar klassen main_menu som kallar på funktionen show_main_menu
class Main_menu:
  def show_main_menu(self):
    #Startar en loop för att hantera felskrivning vid val i menyn samt för att kunna avsluta programmet. 
        run = True
        while run:
          print("\n1. View a country's financial development"
                "\n2. View countries GDP"
                "\n3. View countries Inflation"
                "\n4. View countries Interest rates"
                "\n5. Exit")
          answer = input("-> ").strip()
          # Skapar klassen countries_data och tilldelar den till cd
          cd = Countries_data()
          match answer:
            case "1":
              # Denna klass hanterar och skriver ut en enskillds lands data
              Summary_country()
            # De tre funktionerna nedan skriver ut data för respektive typ. 
            case "2":
              cd.list_countries_gdp()
            case "3":
              cd.list_countries('inflation')
            case "4":
              cd.list_countries('interest_rate')
            # Val 5 stänger programmet genom att sätta run till False och kalla på close_program()
            case "5":
              run = False
              program.close_program()
            case _:
              print("Wrong input, try again..")

  def __init__(self):
    self.show_main_menu()
from .country_summary import summary_country
import program

class main_menu:
  def show_main_menu(self):
        run = True
        while run:
          print("\n1. View a country's financial development\n"
                "\n2. View countries' GDP"
                "\n3. View countries' Inflation"
                "\n4. View countries' interest rates"
                "\n5. Exit")
          answer = input("-> ").strip()
          
          match answer:
            case "1":
              summary_country()
#              case "2":
#              case "3":
#              case "4":
            case "5":
              run = False
              program.close_program()
            case _:
              print("Wrong input, try again..")

  def __init__(self):
    self.show_main_menu()
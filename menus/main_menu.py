from .country_summary import summary_country
import program

class main_menu:
  def show_main_menu(self):
        run = True
        while run:
            print("\n1. Se ett lands finansiella utveckling\n"
                  "\n2. Se länders GDP"
                  "\n3. Se länders Inflation"
                  "\n4. Se länders räntor"
                  "\n5. Avsluta")
            
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
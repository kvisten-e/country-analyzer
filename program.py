from menus.main_menu import Main_menu

#Denna variabel ser till att hålla igång programmet
run_program = True

#Denna klass skapas i main och startar programmet.
class Program:
  def __init__(self):
    #Loop för att köra programmet startas, när run_program blir false så stängs den ner. 
    while run_program != False:
        print(f"\nWelcome to Country Analyser - Europe")
        #Skapar och kallar på klassen
        Main_menu()

# Close_program stänger ner programmet
def close_program():
  global run_program
  run_program = False


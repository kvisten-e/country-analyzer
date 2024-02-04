from menus.main_menu import main_menu

run_program = True

class program:
  def __init__(self):
    while run_program != False:
        print(f"\nWelcome to Country Analyser")
        menu = main_menu()
        
def close_program():
  global run_program
  run_program = False
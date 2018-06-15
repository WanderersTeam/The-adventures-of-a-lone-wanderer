import main_menu, weapons, functions
global gameOn
gameOn = 1

gameOn=main_menu.mainMenu(gameOn)    #Load main menu
if(gameOn==1):
    attributes = main_menu.attributes   #creates variable with attributes chosen in previous function
    functions.show_attributes(attributes)   #shows all attributes of character
    functions.save(attributes)      #saves attributes to file
while(gameOn==1):
    gameOn=functions.whatToDo(attributes, gameOn)

"""placeholder for function testing"""
#while(gameOn == 1):
 #   for level in range(1,11):
  #      loadLevel(level)
   #     level=+1
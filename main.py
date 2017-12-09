import main_menu, weapons, functions

main_menu.mainMenu()    #Load main menu
attributes = main_menu.attributes   #creates variable with attributes chosen in previous function
functions.show_attributes(attributes)   #shows all attributes of character
functions.save(attributes)      #saves attributes to file

attack = functions.attack(attributes)       #creates variable attack with  str + random number from weapon attack range
print(attack)


"""placeholder for function testing"""
##while(gameOn == 1):
##    for level in range(1,11):
##        loadLevel(level)
##        level=+1
##        loadTavern()
##    
input()

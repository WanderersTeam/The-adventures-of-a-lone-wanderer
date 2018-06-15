import random, glob, levels

def save(attributes):
    """Saves attributes to file for later use"""
    with open("saved_game.py", "w") as file:
        file.write("heroName = \'" + str(attributes["heroName"]) + "\'\n")
        file.write("hp = " + str(attributes["hp"]) + "\n")
        file.write("exp = " + str(attributes["exp"]) + "\n")
        file.write("lvl = " + str(attributes["lvl"]) + "\n")
        file.write("strength = " + str(attributes["strength"]) + "\n")
        file.write("mana = " + str(attributes["mana"]) + "\n")
        file.write("hpPotions = " + str(attributes["hpPotions"]) + "\n")
        file.write("manaPotions = " + str(attributes["manaPotions"]) + "\n")
        file.write("weapon = \'" + str(attributes["weapon"]) + "\'\n")
        file.write("weaponAtt = " + str(attributes["weaponAtt"]) + "\n")
        file.close()

def create_new_hero():
    """Asks player for name for new character"""
    global heroName
    heroName = str(input("What is your name, adventurer?\n"))
    return heroName

def show_attributes(attributes):
    """Prints all attributes of character"""
    print("Name: " +  str(attributes["heroName"]) + " | HP: " + str(attributes["hp"]) + " | EXP: " + str(attributes["exp"]) + " | LEVEL: " + str(attributes["lvl"]) +
    "\nSTR: " + str(attributes["strength"]) + " | MANA: " + str(attributes["mana"]) + " | HP Potions: " + str(attributes["hpPotions"]) +
    "\nMana Potions: " + str(attributes["manaPotions"]) + " | Weapon: " + str(attributes["weapon"]))


def attack(attributes):
    """Generates random attack value for held weapon"""
    global attack
    attack = attributes["strength"] + random.randrange(attributes["weaponAtt"][0],attributes["weaponAtt"][1]+1) #uses lowest and highest weapon dmg as range
    print("Attack value: " +str(attack))
    return attack

def help():
    """Prints a list of avaiable commands"""
    print("""List of commands:
    menu - moves you to Main Menu screen
    attack - attack an opponent\n""")

def whatToDo(attributes,gameOn):
    _whatToDo = input("What will you do?\n")
    if(_whatToDo=="help"):
        help()
    elif(_whatToDo=="save"):
        save(attributes)
    elif(_whatToDo=="attack"):
        attack(attributes)
    elif(_whatToDo=="exit"):
        gameOn=exit(gameOn)
    else:
        print("There is no such option\nWrite 'help' to see list of commands")
    return(gameOn)

def exit(gameOn):
    """Exit the game"""
    gameOn=0
    print("See you again")
    return(gameOn)
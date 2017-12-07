def create_new_hero():
    global heroName
    heroName = str(input("What is your name, adventurer?\n"))
    return heroName

def show_attributes(attributes):
    print("Name: " +  heroName + " | HP: " + str(attributes["hp"]) + " | EXP: " + str(attributes["exp"]) + " | LEVEL: " + str(attributes["lvl"]) +
    "\nSTR: " + str(attributes["strength"]) + " | MANA: " + str(attributes["mana"]) + " | HP Potions: " + str(attributes["hpPotions"]) +
    "\nMana Potions: " + str(attributes["manaPotions"]) + " | Weapon: " + str(attributes["weapon"]))

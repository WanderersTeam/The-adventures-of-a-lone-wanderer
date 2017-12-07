main_menu = 1


def mainMenuText():
    print("""    1. New Game
    2. Load Game
    3. Authors
    4. Exit""")
    global choice
    choice = int(input("What to do? [Choose the number]:"))
    return(choice)

def newGameLoad():
    """Import New Game parameters"""
    import new_game
    global attributes
    attributes = {"hp": new_game.hp, "exp": new_game.exp, "lvl": new_game.lvl,
                  "strength": new_game.strength, "mana": new_game.mana,
                  "hpPotions": new_game.hpPotions, "manaPotions": new_game.manaPotions,
                  "weapon": new_game.weapon, "attack": new_game.att}
    return(attributes)

def SavedGameLoad():
    """Import Saved Game parameters"""
    import saved_game
    global attributes
    attributes = {"hp": saved_game.hp, "exp": saved_game.exp, "lvl": saved_game.lvl,
                  "strength": saved_game.strength, "mana": saved_game.mana,
                  "hpPotions": saved_game.hpPotions, "manaPotions": saved_game.manaPotions,
                  "weapon": saved_game.weapon, "attack": saved_game.att}
    return(attributes)
def authors():
    """Show Authors of the game"""
    print("""\n   WanderersTeam:\n
    Alicja Olejniczak\n
    Bartosz Zawadzki\n
    Klaudia Slawinska\n\n""")
def exit():
    """Exit the game"""
    print("See you again")
    

def mainMenu():
    while(main_menu == 1):
        mainMenuText()
        if(choice == 1):
            newGameLoad()
            print("Started a new game")
            break
        elif(choice == 2):
            SavedGameLoad()
            print("Loaded a saved game")
            break
        elif(choice == 3):
            authors()
        elif(choice == 4):
            exit()
            break


import functions
global main_menu
main_menu = 1


def mainMenuText():
    """Prints options for start of the game"""
    print("""    1. New Game
    2. Load Game
    3. Authors
    4. Exit""")
    global choice
    choice = input("What to do? [Choose the number]:")
    return(choice)

def newGameLoad():
    """Import New Game parameters"""
    import new_game
    global attributes
    attributes = {"heroName": new_game.heroName, "hp": new_game.hp, "exp": new_game.exp, "lvl": new_game.lvl,
                  "strength": new_game.strength, "mana": new_game.mana,
                  "hpPotions": new_game.hpPotions, "manaPotions": new_game.manaPotions,
                  "weapon": new_game.weapon, "weaponAtt": new_game.weaponAtt}
    return(attributes)

def SavedGameLoad():
    """Import Saved Game parameters"""
    import saved_game
    global attributes
    attributes = {"heroName": saved_game.heroName, "hp": saved_game.hp, "exp": saved_game.exp, "lvl": saved_game.lvl,
                  "strength": saved_game.strength, "mana": saved_game.mana,
                  "hpPotions": saved_game.hpPotions, "manaPotions": saved_game.manaPotions,
                  "weapon": saved_game.weapon, "weaponAtt": saved_game.weaponAtt}
    return(attributes)
def authors():
    """Show Authors of the game"""
    print("""\n   WanderersTeam:\n
    Alicja Olejniczak\n
    Bartosz Zawadzki\n
    Klaudia Slawinska\n\n""")


def mainMenu(gameOn):
    """Main part of Main Menu in game"""
    while(main_menu == 1):
        mainMenuText()
        if(choice == '1'):
            newGameLoad()
            print("Started a new game")
            attributes["heroName"] = functions.create_new_hero()     #changes herName to chosen Name
            gameOn=1
            break
        elif(choice == '2'):
            SavedGameLoad()
            gameOn=1
            print("Loaded a saved game")
            break
        elif(choice == '3'):
            authors()
        elif(choice == '4'):
            gameOn=functions.exit(gameOn)
            break
        else:
            print("We don`t do that here\n")
            continue
    return(gameOn)

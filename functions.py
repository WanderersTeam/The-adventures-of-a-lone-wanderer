import new_game

attributes = {"hp": new_game.hp, "exp": new_game.exp, "lvl": new_game.lvl,
                  "strength": new_game.strength, "mana": new_game.mana,
                  "hpPotions": new_game.hpPotions, "manaPotions": new_game.manaPotions,
                  "weapon": new_game.weapon, "attack": new_game.att}

def save(attributes):
    with open("saved_game.py", "w") as file:
        file.write("hp = " + str(attributes["hp"]) + "\n")
        file.write("exp = " + str(attributes["exp"]) + "\n")
        file.write("lvl = " + str(attributes["lvl"]) + "\n")
        file.write("strength = " + str(attributes["strength"]) + "\n")
        file.write("mana = " + str(attributes["mana"]) + "\n")
        file.write("hpPotions = " + str(attributes["hpPotions"]) + "\n")
        file.write("manaPotions = " + str(attributes["manaPotions"]) + "\n")
        file.write("weapon = " + str(attributes["weapon"]) + "\n")
        file.write("attack = " + str(attributes["attack"]) + "\n")
        file.close()

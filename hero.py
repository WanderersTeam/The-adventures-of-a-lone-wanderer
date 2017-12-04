#Statistics of Main Hero for new game and saved game.

def hero_att_new():
    attributes = {"hp" : 40, "strength" : 10, "mana" : 10}
    inventory = {"sword" : "s_sword", "shield" : "s_shield", "armor" : "s_armor",
                 "phealth" : "s_phealth", "pmana" : "s_mana"}
    return attributes, inventory

def hero_saved_game():
    return 0


show = hero_att_new()
print(show)
print(hero_att_new())

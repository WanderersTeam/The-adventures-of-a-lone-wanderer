import random
global tier0, tier1
tier0={"Wooden Sword": [1,2]}
tier1={"Iron Sword": [2,4]}

def chooseTier0():
    tier0Names=[]
    global weapon
    for weapon in tier0.keys():
        tier0Names.append(weapon)
    weapon = random.choice(tier0Names)
    return weapon

def chooseTier1():   
    tier1Names=[]
    global weapon
    for weapon in tier1.keys():
        tier1Names.append(weapon)
    weapon = random.choice(tier1Names)
    return weapon

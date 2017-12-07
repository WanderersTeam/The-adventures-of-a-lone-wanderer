import weapons, random

hp = 40
exp = 0
lvl = 1
strength = 10
mana = 10
hpPotions = 2
manaPotions = 1
weapon = weapons.chooseTier0()
weaponAtt = weapons.tier0[weapon]
att = strength + random.randrange(weaponAtt[0],weaponAtt[1])

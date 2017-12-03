gra = 1
hp=50
stamina=12
mana=10
def cls(): print("\n" * 100)

while(gra == 1):
    cls()
    print("HP: "+str(hp)+" Stamina: "+str(stamina)+" Mana: "+str(mana))
    gra = int(input("Gra: "))

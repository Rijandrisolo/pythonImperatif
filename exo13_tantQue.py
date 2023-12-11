chiffre = int(input("chiffre de départ ? "))
while not 1<=chiffre<=10 :
    print("le chiffre doit être entre 1 et 10")
    chiffre = int(input("chiffre de départ ? "))
print("le chiffre est ", chiffre)
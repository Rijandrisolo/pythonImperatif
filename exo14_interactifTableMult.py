chiffre = int(input("chiffre de départ ? "))
table = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while not 1<=chiffre<=10 :
    print("le chiffre doit être entre 1 et 10")
    chiffre = int(input("chiffre de départ ? "))
for i in table :
    print(chiffre, "*", i, " = ", chiffre * i)
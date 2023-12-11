chiffre = int(input("chiffre de départ ? "))
ch = 0
print("le nombre est ", chiffre)
for num in range(1, chiffre+1) :
    ch +=num
print("Le total est ", ch)

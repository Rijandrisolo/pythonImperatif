chiffre = int(input("chiffre de départ ? "))
iter = int(input("jusqu'à ? "))
ch = chiffre
tab = []
while ch <= chiffre + iter :
    tab.append(ch)
    ch +=1

print(tab)
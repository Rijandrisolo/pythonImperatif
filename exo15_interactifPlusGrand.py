chiffre = int(input("chiffre de départ ? "))
table = []
table.append(chiffre)
ch=1
while ch<=9 :
    chiffre = int(input("chiffre de départ ? "))
    table.append(chiffre)
    ch += 1
print("Les chiffres que vous avez saisi ", table)
print("le plus grand est ", max(table))
liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
vmoy = sum(liste) / len(liste)
vmoy2 = 0
vlen = 0

for x in liste :
    if x >= 0 :
        vlen += 1
        vmoy2 += x


vmoy2 = vmoy2/vlen
print("la moyenne est ", vmoy)
print("la moyenne des nombres positifs est ", vmoy2)

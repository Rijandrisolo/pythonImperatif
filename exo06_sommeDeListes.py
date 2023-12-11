liste1 = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
liste2 = [-1, 12, 17, 14, 5, -9, 0, 18, -6, 0, 4, -13, 5, 7, -2, 8, -1]
resultat = []
total = 0
l2 = len(liste2)
l1 = len(liste1)
if l2>l1 :
    longueur = l2
else :
    longueur = l1

for i in range(longueur) :
    total = 0
    if liste2[i] & liste1[i] :
        total = liste1[i] + liste2[i]

    else :
        total = liste2[i]

    resultat.append(total)
print("La liste du résultat est ", resultat)
print("---------------impression avec une boucle-----------------")
for l in resultat :
    print(l)
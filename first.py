#boucle pair
print("chiffres pair de 0 à 10")
for i in range(10):
    if i%2 == 0:
        print(i)
print("----------------------------")
print("chiffres impair de 0 à 10")
#boucle impair
for i in range(10):
    if i%2 == 1:
        print(i)

print("----------------------------")

liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
pos = 0
for l in liste:
    print(l)
print("----------------------------")
print("liste nombres positifs")
for l in liste:
    if l >= 0 :
        pos +=1
        print(l)
print("----------------------------")
print("le nombre d'éléments positifs est", pos)



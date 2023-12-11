def entiers(liste, min, max):
    total = 0
    min = 10
    max = 15
    for l in liste:

            if isinstance(l, int) and min <= l <= max:
                   total += 1
            elif isinstance(l, list):

                   total += entiers(l, min, max)


    return total


# Exemple d'utilisation avec votre liste
liste = [28, [12, [13, 1], -2, [[4, 5], -5]]]
total = entiers(liste, min, max)

print("Le nombre d'entiers dans la liste est : ", total)
def entiers(liste):
    total_entiers = 0

    for l in liste :
        if isinstance(l, int):
            total_entiers += 1
        elif isinstance(l, list):
            total_entiers += entiers(l)

    return total_entiers


# Exemple d'utilisation avec votre liste
liste = [28, [12, [13, 1], -2, [[4, 5], -5]]]
total = entiers(liste)

print("Le nombre d'entiers dans la liste est : ", total)
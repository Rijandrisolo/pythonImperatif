liste1 = [1, 15, -3, 8, 7, 4, -2, 28, -1, 17, 2, 3, 0, 14, -4]
liste2 = [3, -8, 17, 5, -1, 4, 0, 6, 2, 11, -5, -4, 8]
total = 0
for l1 in liste1 :
    for l2 in liste2 :
        if l1 == l2 :
            total += 1
            print("En liste1", l1, "en liste2 ", l2)
print("Il y a ", total, " valeurs communes")
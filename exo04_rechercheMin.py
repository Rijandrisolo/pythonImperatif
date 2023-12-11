liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, -4, 14]
vmin = liste[-1]
for l in liste :
    if vmin>=l :
        vmin=l
print("la valeur min est ", vmin)
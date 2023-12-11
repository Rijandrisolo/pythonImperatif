# exo 1 addition
def addition(a, b):
    print("addition", a + b)


# exo_2 palindrome
def is_palindrome(char):
    response = "non"
    for i in range(len(char) // 2):
        if char[i] == char[-i - 1]:
            response = "oui"
            print(char[i], char[-i - 1])
    print(response)
    #[::-1]

# exo_3 entre les min et max
def min_max(a, b, c):
    r = range(a, b)
    print("fourchette", r)
    d = []
    for i in c:
        if i in range(a, b):
            d.append(i)
            print(d)
    print("la liste est", c)
    print("Les valeurs entre ", a, "et", b, "sont", d)


# exo_4 calcul moyenne
def moyenne(a):
    b = len(a)
    print("La longueur de la liste est :", b)
    val = 0
    for i in a:
        val += i
        print("somme des valeurs", val)
    print("total", val)
    val = val / b
    print("la moyenne", val)
    #sum(liste/len(liste))

print("------------tp05-------------")
print("--------- addition---------")
addition(4, 5)
print("--------- palindrome---------")
is_palindrome("radare")
print("--------- entre min et max---------")
min_max(2, 8, [1, 5, 6, 0, 7])
print("--------- moyenne d'une liste---------")
moyenne([10, 5, 6, 5, 7])

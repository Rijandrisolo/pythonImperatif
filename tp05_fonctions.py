
#exo 1 addition
def addition(a,b) :
    print("addition", a+b)
#exo_2 palindrome
def is_palindrome(char):
    response ="non"
    for i in range(len(char)//2):
       if char[i] == char[-i-1]:
            response = "oui"
            print(char[i], char[-i-1])
    print(response)
#exo_3 entre les min et max
def min_max(a,b, c) :
    r = range(a, b)
    print("fourchette", r)
    d = []
    for i in c :
        if i in range(a, b) :
            d.append(i)
            print(d)
    print("les valeurs sont", c)
    print("Les valeurs entre ", a, "et", b, "sont", d)

#exo_4 calcul moyenne
def moyenne(a) :

    b = len(a)
    print(b)
    val = 0
    for i in a :
        val += i
        print("intérieur", val)
    print("total", val)
    val =val/b
    print("la moyenne", val)

print("--------- addition---------")
addition(4,5)
print("--------- palindrome---------")
is_palindrome("bab")
print("--------- entre min et max---------")
min_max(2, 8, [1, 5, 6, 0, 7])
print("--------- moyenne d'une liste---------")
moyenne([10, 5, 6, 5, 7])





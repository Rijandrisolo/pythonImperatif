essai = 10
#tableau pour mettre les mots venants de mots.txt
tableau=[]
#permet de boucler pour afficher dans le terminal les lettres trouvées
tabmot=[]
#affichage des lettres trouvées
tabjuste=[]
#######################################################
f=open('mots.txt')
for line in f.readlines() :
    tableau.append(line.strip())
f.close()
#mot=input("Saisir le mot à chercher :")
nombre = len(tableau)
chercher = int(input(f"Choisissez un chiffre de 1 à {nombre} pour avoir le mot que vous devez chercher : "))
mot = (tableau[chercher])
#print("le mot à chercher", mot)
lettre = len(mot)
for i in range (len(mot)) :
    tabjuste.append("*")
print(tabjuste)
print("Le mot à chercher est de :", lettre, "lettres. Vous avez ", essai, "essais")
while essai>0 :
    motSaisi = input("Votre mot : ")
    tabmot = []
    for lettre in motSaisi :
       for mo in mot :
           if(lettre.upper() == mo.upper()) :
              tabmot.append(lettre.upper())
    tabmot = set(tabmot)
    print("Vous avez trouvé ", len(tabmot), "lettre(s)")
    for tabmo in tabmot :
        for i in range (len(mot)) :
            if mot[i] == tabmo :
                tabjuste[i] = tabmo

    print(str(tabjuste).upper())
   # if(tabjuste.count('*') == 0) :
    if(motSaisi.upper() == mot.upper()) :
        print("bravo, vous avez trouvé le mot")
        print("\O/")
        print(mot)
        break
    essai -=1
    if essai > 0 :
        print("Vous avez encore : ", essai, "essai(s)")
    if(essai == 0) :
        print("vous avez perdu")
        print("le mot était", mot.upper())
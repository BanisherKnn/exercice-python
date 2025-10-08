#Exercice 1
semaine = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for jours in semaine:
    if jours in["lundi","mardi","mercredi","jeudi"]:
        print (f"on est {jours} puisque c'est un jour de la semaine je travail")
    elif jours == ("vendredi"):
        print ("nous sommes bientôt le weekend car on est vendredi")
    else:
        print(f"repos car on est en weekend le {jours}")




#Exercice 2
list = [8,4,6,1,5]
copielist = list.copy()        # Copie de la list pour pouvoir la modifier.
copielist.sort()               # Pemret de trier la liste.
print (copielist[0])           # le "[0]" permet de print seulement la 1ere valeur de la liste 




# Complément de l'exercice 2
list = [8,4,6,1,5]
print (min(list))



#Exercice 3
note = [14,9,13,15,12]
resultatmoyenne = notelist.copy()                        # Copie de la list pour pouvoir la modifier.
resultat = sum(notelist)                                 # Calcule de la moyenne des notes.
print ((f"La moyenne est de {resultat/len(notelist)}"))  # "/len" permet de calculer le nombre de valeur dans la list.
print (("La note la plus basse est"),min(note),("\nLa note la plus élevé est"),max(note)) # Calcule du minimum et du maximum des notes.



# Complément de l'exercice 3
notelist = [14,9,13,15,12]
resultatmoyenne = notelist.copy()
resultat = sum(notelist)
print (resultat/len(notelist))



#Exercice 4
listpair = []
listimpair = []
for i in range(21):
    if i<=10:
       if i%2 == 0:
           listpair.append(i)
    else:
        if i>10:
            if i%2 == 1:
                listimpair.append(i)
print (listpair,listimpair)

#Exercice 5

colonne = 0
ligne = 0.5
matrice = ([0,1,
            1,0])
for i in matrice:
    ligne += 0.5
    colonne += 1
    if colonne > 2:
        colonne = 1
    print (f"Le nombre {[i]} de la ligne {int(ligne)} et de la colonne {colonne}")


#Exercice 6

for i in range(11):
    print("*"*i)


#Exercice 7 

import random   # Cette ligne doit être tout en haut du fichier

# Position initiale de la puce
position = 0

# Compteur de sauts
nb_sauts = 0

# Boucle jusqu'à atteindre la position 5
while position != 5:
    saut = random.choice([-1, 1])
    position += saut
    nb_sauts += 1

    print(f"Saut {nb_sauts} : la puce est maintenant en position {position}")

print(f"\nLa puce est arrivée à la position 5 en {nb_sauts} sauts.")
    
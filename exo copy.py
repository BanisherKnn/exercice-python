import random   # ⚠️ Cette ligne doit être tout en haut du fichier

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
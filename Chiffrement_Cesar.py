# Chiffrement de César

# Message à chiffrer
message = """Les mathématiques sont fascinantes. Elles permettent de résoudre 
des problèmes, de comprendre le monde qui nous entoure et de construire des 
technologies innovantes. Chiffrons ce message avec le chiffrement de César !"""
# Saisie de la clé de chiffrement
k = int(input("Saisissez la clé (entier positif) : "))

# Liste pour stocker les résultats du chiffrement
liste = []

# Chiffrement du message
for lettre in message:
    # Utilisation de la fonction ord() pour obtenir la valeur ASCII de la lettre
    # et ajout de la clé, modulo 256 pour rester dans la plage des caractères ASCII
    chiffrage = (ord(lettre) + k) % 256
    liste.append(chiffrage)

print("\nLe chiffrement donne (en codes ASCII) : ", liste)

# Liste pour stocker les résultats du déchiffrement
liste2 = []

# Déchiffrement du message
for cpt in liste:
    # Soustraction de la clé et utilisation de modulo 256 pour rester dans la plage ASCII
    nbr = (cpt - k) % 256
    # Utilisation de la fonction chr() pour obtenir la lettre correspondant à la valeur ASCII
    dechiffrage = chr(nbr)
    liste2.append(dechiffrage)

# Création de la chaîne de caractères déchiffrée à partir de la liste
messageF = ''.join(liste2)

# Affichage du message déchiffré
print("\nMessage déchiffré : ", messageF)

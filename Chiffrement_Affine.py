#Chiffrement Affine
def chiffre_affine(x, a, b, n): 
    liste = [] 
    for lettre in a: 
        # Chiffrement affine : 
        chiffrage = ((ord(lettre) * x) + b) % n 
        liste.append(chiffrage) 
    # Affichage des résultats du chiffrement 
    print("Le chiffrement donne: ", liste) 
    return liste 

def dechiffre_affinre(liste, x, b, n): 
    liste2 = [] 
    # Calcul de l'inverse  de x modulo n 
    z = euclideEtendu(x, n) 
    x_inverse = z[1] 
    for cpt in liste: 
        # dechiffrage de chaque element de la liste 
        nbr = ((cpt - b) * x_inverse) % n 
        # Conversion du nombre déchiffré en caractère ASCII 
        dechiffrage = chr(nbr) 
        liste2.append(dechiffrage) 
    # concatenation de la chaîne de caractères déchiffrée 
    messageF = ''.join(liste2) 
    print("Résultat: ", messageF) 

# Texte à chiffrer et déchiffrer 
a = "La cryptographie est l'art d'écrire des messages de manière à les protéger des personnes non autorisées. Elle repose sur des algorithmes et des clés pour garantir la confidentialité, l'intégrité et l'authenticité des données." 
x = 15   # Coefficient 
b = 54   # Clé 
n = 256   # Modulo 

# Appel de la fonction de chiffrement affine 
p = chiffre_affine(x, a, b, n) 

# Appel de la fonction de déchiffrement affine 
dechiffre_affinre(p, x, b, n)
# El Gamal  

# Fonction d'échange de clé
def echange_(s, p, a):
    # Vérifie si a est plus grand que p 
    if p < a: 
        print("Re-saisir les valeurs de a et p") 
        a = int(input("Entrez la valeur de a: "))
        p = int(input("Entrez la valeur de p: "))

    # Vérifie si p est un nombre premier
    if not isprime_eratosthene(p):
        print(f"{p} n'est pas premier !")
        exit()
       
    # Calcul de Q = a^s mod p
    Q = expo_mod(a, s, p)
    return Q


# Fonction de chiffrement du message
def Chiffrage_Mess(M, Q, p, k, a):
    # Si M est plus grand que p, réduire M modulo p
    if M > p:
        M = M % p

    # Calcul de c1 = a^k % p
    C1 = expo_mod(a, k, p)

    # Calcul de c2 = (M * Q^k) % p
    C2 = (M * expo_mod(Q, k, p)) % p

    return C1, C2

# Fonction de déchiffrement du message
def Mess_dech(C1, C2, p, s):
    # Calcul du message déchiffré M2 = (C1^(p-1-s) * C2) % p
    M2 = (expo_mod(C1, p - 1 - s, p) * C2) % p 

    print("Message déchiffré:", M2)

# Définition des variables
s = 15  # Clé secrète
p = 479  # Nombre premier
a = 74  # Nombre inférieur à p
k = 43  # Clé de chiffrement du message
M = 228  # Message à chiffrer

# Appel de la fonction echange_ pour obtenir Q (clé publique)
Q = echange_(s, p, a)
print(f"La clé publique: ({p}, {a}, {Q})")

# Appel de la fonction Chiffrage_Mess pour chiffrer le message
C1, C2 = Chiffrage_Mess(M, Q, p, k, a)
print(f"Le message chiffré: ({C1}, {C2})")

# Appel de la fonction Mess_dech pour déchiffrer le message
M_déchiffré = Mess_dech(C1, C2, p, s)
print(f"Message déchiffré: {M_déchiffré}")
import numpy as np  # type: ignore
import matplotlib.pyplot as plt   # type: ignore
import secrets
import string

def euclideEtendu(a, b):
    # Initialisation des variables
    u = 1  
    v = 0  
    up = 0  
    vp = 1  

    while b != 0:  # Continue tant que le reste n'est pas nul
        q = a // b  # Quotient de la division euclidienne
        r = a % b  # Reste de la division euclidienne
        a = b  # Actualisation de a
        b = r  # Actualisation de b

        # Actualisation des coefficients de Bézout
        udp = u - q * up
        vdp = v - q * vp

        # Permutation des coefficients
        u = up
        v = vp
        up = udp
        vp = vdp

    return a, u, v  # Retourne le PGCD et les coefficients de Bézout




# Exemple d'utilisation
a = 17
b = 13
pgcd, u, v = euclideEtendu(a, b)
print(f"Le PGCD de {a} et {b} est {pgcd}. Les coefficients de Bézout sont u = {u} et v = {v}.")


def inverseModuloN(a, n):
    pgcd, u, v = euclideEtendu(a, n)  # Calcule le PGCD et les coefficients de Bézout
    if pgcd == 1:  # L'inverse modulaire n'existe que si PGCD(a, n) = 1
        return u % n  # L'inverse modulaire est le coefficient u modulo n
    else:
        return "Pas d'inverse."



# Exemple d'utilisation
print("L'inverse modulaire est", inverseModuloN(17, 13),  "[13]")  # Affiche l'inverse modulaire de 17 modulo 43
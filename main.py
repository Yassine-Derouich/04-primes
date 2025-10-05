""" Module fournissant la fonction racine carré SQRT """
from math import sqrt

#### Fonction secondaire


def isprime(p: int)->bool:
    """ 
    Déterminer si un nombre est premier.

    args:
    p (entier): nombre à vérifier sa primalité

    returns:
    bool: True si p est premier et False sinon
    """
    if p == 1:
        return False
    if p == 2:
        return True
    limite_diviseur = int(sqrt(p))+1
    for diviseur in range(2, limite_diviseur):
        if p % diviseur == 0:
            return False
    return True

#### Fonction principale

def main():
    """
    Indique si les nombres n de a à b sont primaire ou non

    Args:
        None

    Returns:
        None mais appelle isprime(n) qui retourne un bool
    """
    a: int = 2
    b: int = 45
    for n in range(a,b):
        if isprime(n):
            print(f"{n} est un nombre premier", end=", ")

    print()


if __name__ == "__main__":
    main()

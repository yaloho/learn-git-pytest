from typing import Union

# Définition d'un type pour les nombres (entiers et flottants)
Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Retourne la somme de a et b.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        La somme de a et b
    """
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """
    Retourne le résultat de la soustraction de b à a.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        Le résultat de a - b
    """
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """
    Retourne le produit de a et b.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        Le produit de a et b
    """
    return a * b

def divide(a: Number, b: Number) -> Number:
    """
    Retourne le résultat de la division de a par b.

    Args:
        a: Premier nombre (dividende)
        b: Deuxième nombre (diviseur)

    Returns:
        Le résultat de a / b

    Raises:
        ValueError: Si b est 0
    """
    if b == 0:
        raise ValueError("Division par zéro non autorisée")
    return a / b

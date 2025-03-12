# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 12:58:07 2025

@author: ahmad
"""

def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # Inverse la chaîne de caractères en utilisant le slicing
    return s[::-1]


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    vowels = "aeiouAEIOU"  # Liste des voyelles, incluant les majuscules et minuscules
    return sum(1 for char in s if char in vowels)  # On compte chaque voyelle présente dans la chaîne


def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    # On ignore les espaces et on met tout en minuscules pour ignorer la casse
    s = ''.join(s.split()).lower()
    # Vérifie si la chaîne est égale à sa version inversée
    return s == s[::-1]


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    # On découpe la chaîne en mots, on met chaque mot en majuscule et on rejoint les mots avec des espaces
    return ' '.join(word.capitalize() for word in s.split())

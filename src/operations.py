import math


def addition(x: float, y: float) -> float:
    """Retourne l'addition de deux nombres."""
    return x + y


def soustraction(x: float, y: float) -> float:
    """Retourne la soustraction de deux nombres."""
    return x - y


def multiplication(x: float, y: float) -> float:
    """Retourne la multiplication de deux nombres."""
    return x * y


def division(x: float, y: float) -> float:
    """Retourne la division de x par y."""
    if y == 0:
        raise ValueError("Division par zéro impossible.")
    return x / y


def puissance(x: float, y: float) -> float:
    """Retourne x élevé à la puissance y."""
    return x ** y


def racine_carree(x: float) -> float:
    """Retourne la racine carrée de x."""
    if x < 0:
        raise ValueError("La racine carrée d'un nombre négatif est impossible.")
    return math.sqrt(x)
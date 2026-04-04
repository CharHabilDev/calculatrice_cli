import argparse

from operations import(
    addition,
    soustraction,
    multiplication,
    division,
    puissance,
    racine_carree
)


def cmd_add(args: argparse.Namespace) -> None:
    """
    Affiche l'addition de deux nombres.

    Args: 
        args: arguments de la ligne de commande, contenant notamment
            args.num1 et args.num2.

    Returns:
        Rien.
    """
    resultat = addition(args.num1, args.num2)
    print(f"Résultat : {args.num1} + {args.num2} = {resultat}")


def cmd_sous(args: argparse.Namespace) -> None:
    """
    Affiche la soustraction de deux nombres.

    Args:
        args: arguments de la ligne de commande, contenant notamment
            args.num1 et args.num2.

    Returns: 
        Rien.
    """
    resultat = soustraction(args.num1, args.num2)
    print(f"Résultat : {args.num1} - {args.num2} = {resultat}")


def cmd_mult(args: argparse.Namespace) -> None:
    """
    Affiche la multiplication de deux nombres.

    Args:
        args: arguments de la ligne de commande, contenant notamment
            args.num1 et args.num2.

    Returns: 
        Rien.
    """
    resultat = multiplication(args.num1, args.num2)
    print(f"Résultat : {args.num1} * {args.num2} = {resultat}")


def cmd_div(args: argparse.Namespace) -> None:
    """
    Affiche la division de args.num1 par args.num2.

    Args:
        args: arguments de la ligne de commande, contenant notamment
            args.num1 et args.num2.

    Returns: 
        Rien.
    """
    resultat = division(args.num1, args.num2)
    print(f"Résultat : {args.num1} / {args.num2} = {resultat:.3f}")


def cmd_puis(args: argparse.Namespace) -> None:
    """
    Affiche args.num1 élevé à la puissance args.num2.

    Args:
        args: arguments de la ligne de commande, contenant notamment
            args.num1 et args.num2.

    Returns: 
        Rien.
    """
    resultat = puissance(args.num1, args.num2)
    print(f"Résultat : {args.num1} ^ {args.num2} = {resultat}")


def cmd_sqrt(args: argparse.Namespace) -> None:
    """
    Affiche la racine carrée de args.num.

    Args:
        args: arguments de la ligne de commande, contenant notamment
            args.num.

    Returns: 
        Rien.
    """
    resultat = racine_carree(args.num)
    print(f"Résultat : √{args.num} = {resultat:.3f}")



def main() -> None:

    # Configuration du parser
    parser = argparse.ArgumentParser(
        description="Calculatrice en CLI."
    )

    # Création du gestionnaire de sous-commandes 
    subparsers = parser.add_subparsers(dest="operation", required=True)

    # Commande add
    add_parser = subparsers.add_parser('add', help="Opérateur d'addition.")
    add_parser.add_argument('num1', type=float, help="Premier nombre")
    add_parser.add_argument('num2', type=float, help='Deuxième nombre')
    add_parser.set_defaults(func = cmd_add) #Lecture de la fonction

    # Commande sous
    sous_parser = subparsers.add_parser('sous', help="Opérateur de soustraction.")
    sous_parser.add_argument('num1', type=float, help="Premier nombre")
    sous_parser.add_argument('num2', type=float, help='Deuxième nombre')
    sous_parser.set_defaults(func = cmd_sous) #Lecture de la fonction

    # Commande mult
    mult_parser = subparsers.add_parser('mult', help="Opérateur de multiplication.")
    mult_parser.add_argument('num1', type=float, help="Premier nombre")
    mult_parser.add_argument('num2', type=float, help='Deuxième nombre')
    mult_parser.set_defaults(func = cmd_mult) #Lecture de la fonction

    # Commande div
    div_parser = subparsers.add_parser('div', help="Opération de division.")
    div_parser.add_argument('num1', type=float, help="Premier nombre")
    div_parser.add_argument('num2', type=float, help='Deuxième nombre')
    div_parser.set_defaults(func = cmd_div) #Lecture de la fonction

    # Commande puis
    puis_parser = subparsers.add_parser('puis', help="Opérateur de puissance.")
    puis_parser.add_argument('num1', type=float, help="Base")
    puis_parser.add_argument('num2', type=float, help='Exposant')
    puis_parser.set_defaults(func = cmd_puis) #Lecture de la fonction

    # Commande sqrt
    sqrt_parser = subparsers.add_parser('sqrt', help="Opération de racine carrée.")
    sqrt_parser.add_argument('num', type=float, help="Nombre")
    sqrt_parser.set_defaults(func = cmd_sqrt) #Lecture de la fonction

    #Exécution
    args = parser.parse_args()

    # Appelle de la fonction associée à la commande
    args.func(args)

if __name__ == "__main__":
    main()
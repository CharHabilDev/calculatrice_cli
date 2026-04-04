from operations import (
    addition,
    soustraction,
    multiplication,
    division,
    puissance,
    racine_carree
)


def afficher_menu() -> None:
    print("=== CALCULATRICE CLI INTERACTIVE ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Racine carrée")
    print("7. Quitter")


def demander_nombre(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Erreur : tu dois entrer un nombre valide.")

    
def main() -> None:
    while True:
        afficher_menu()
        choix = input('Ton choix : ').strip()

        if choix == "7":
            print("Fermeture de la calculatrice...")
            break

        try:
            if choix == "1":
                x = demander_nombre('Entrer le premier nombre : ')
                y = demander_nombre('Entrer le deuxième nombre : ')
                resultat = addition(x, y)
                print(f"Résultat : {x} + {y} = {resultat}")

            elif choix == "2":
                x = demander_nombre('Entrer le premier nombre : ')
                y = demander_nombre('Entrer le deuxième nombre : ')
                resultat = soustraction(x, y)
                print(f"Résultat : {x} - {y} = {resultat}")

            elif choix == "3":
                x = demander_nombre('Entrer le premier nombre : ')
                y = demander_nombre('Entrer le deuxième nombre : ')
                resultat = multiplication(x, y)
                print(f"Résultat : {x} * {y} = {resultat}")

            elif choix == "4":
                x = demander_nombre('Entrer le premier nombre : ')
                y = demander_nombre('Entrer le deuxième nombre : ')
                resultat = division(x, y)
                print(f"Résultat : {x} / {y} = {resultat:.3f}")

            elif choix == "5":
                x = demander_nombre('Entrer la base : ')
                y = demander_nombre('Entrer l\'exposant : ')
                resultat = puissance(x, y)
                print(f"Résultat : {x} ^ {y} = {resultat:.3f}")

            elif choix == "6":
                x = demander_nombre('Entrer un nombre : ')
                resultat = racine_carree(x)
                print(f"Résultat : √{x}  = {resultat:.3f}")

            else:
                print("Erreur : choix invalide. Veuillez choisir une option de 1 à 7.")

        except ValueError as erreur:
            print(f"Erreur : {erreur}")


if __name__ == "__main__":
    main()
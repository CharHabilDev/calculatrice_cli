# Calculatrice CLI

Une calculatrice en ligne de commande développée en Python pour pratiquer les bases :
fonctions, conditions, boucles, gestion d'erreurs, tests unitaires et organisation de projet.

## Objectifs pédagogiques 

Ce projet m'aide à apprendre:

- les fonctions
- les conditions
- les boucles
- la conversion de types 
- la gestion des erreurs avec `try/except`
- les tests unitaires avec `unittest`
- l'organisation propre d'un projet Python

## Fonctionnalités

### Version 1 - Interactive
- addition 
- soustraction
- multiplication
- division 
- puissance
- racine carrée 
- gestion de la division par zéro
- gestion des entrées invalides
- plusieurs opérations dans une même session

### Version 2 - CLI avec `argparse`
- exécution directe depuis le terminal
- addition 
- soustraction
- multiplication
- division 
- puissance
- racine carrée 

## Structure du projet

````text
calculatrice_cli/
|
|-- src/
|   |-- __init__.py
|   |-- operations.py
|   |-- interactive_app.py
|   `-- cli_app.py
|
|-- tests/
|   `-- test_operations.py
|
|-- README.md
`-- .gitignore
````

## Prérequis

* Python 3 installé sur la machine

## Lancer le projet

### Version interactive

````bash
python src/interactive_app.py
````

### Version CLI avec arguments

Exemples : 

````bash
python src/cli_app.py add 2 5
python src/cli_app.py sous 8 3
python src/cli_app.py mult 4 6
python src/cli_app.py div 10 2
python src/cli_app.py puis 2 3
python src/cli_app.py sqrt 9
````

## Lancer les tests

````bash
python -m unittest discover -s tests
````

## Exemple de sortie

### Mode interactif

````text
=== CALCULATRICE CLI INTERACTIVE ===
1. addition 
2. soustraction
3. multiplication
4. division 
5. puissance
6. racine carrée 
7. Quitter
````

## Gestion des erreurs

Le programme gère :

* la division par zéro
* la racine carrée d'un nombre négatif
* les entrées non numériques
* les choix invalides

## Évolution du projet

* `v1.0.0` : calculatrice interactive
* `v2.0.0` : calculatrice avec arguments CLI

## Auteur

Projet réalisé par Char-Habil dans le cadre de l'apprentissage de Python
from game2048.constants import *


def read_size_grid():
    size = input("Entrez la taille de la grille (entier) : ")
    while True:
        try:
            size = int(size)
            print(size)
            return size
        except ValueError:
            print("Commande non valide")
            size = input("Entrez la taille de la grille (entier) : ")


def read_theme_grid():
    theme = input("Entrez le thème du jeu : ")
    while True:
        if theme not in THEMES.keys():
            print("Commande non valide")
            theme = input("Entrez le thème du jeu : ")
        else:
            print(theme)
            return theme


def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)): ")
    while True:
        if move not in COMMANDS:
            print("Commande non valide")
            move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)): ")
        else:
            print(move)
            return move


read_size_grid()
read_theme_grid()
read_player_command()
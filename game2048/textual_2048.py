from game2048.grid_2048 import *


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
            return move


def ask_and_read_grid_size():
    return read_size_grid()


def ask_and_read_grid_theme():
    return THEMES[str(read_theme_grid())]


def ask_and_read_player_command():
    command = read_player_command()
    index = COMMANDS.index(command)
    return COMMANDS_FULL[index]


def game_play():
    size = ask_and_read_grid_size()
    theme = ask_and_read_grid_theme()
    grid = init_game(size)
    print(grid_to_string_with_size_and_theme(grid, theme, size))
    while not is_game_over(grid):
        move = ask_and_read_player_command()
        grid = move_grid(grid, move)
        grid_add_new_tile(grid)
        print(grid_to_string_with_size_and_theme(grid, theme, size))
    if is_winning_game(grid):
        print("Bravo, vous avez gagné !")
    else:
        print("Désolé, vous avez perdu... Réessayez !")


if __name__ == '__main__':
    game_play()
    exit(1)

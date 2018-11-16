from tkinter import *
from game2048.grid_2048 import *


class Game:
    def __init__(self):
        self.grid = init_game()
        self.grid_size = 4
        self.over = is_game_over(self.grid)
        self._create_ui()

    def start(self):
        self.root.mainloop()

    def _create_ui(self):
        self.root = Tk()
        self.root.title('2048 - root')
        self.root.geometry('200x200+0+0')
        self.top = Toplevel(self.root)
        self.top.title('2048 - top')
        self.top.geometry('200x200-200+0')
        self.top.transient(self.root)

        self.background = Frame(self.top, bd=1, relief='solid')
        self.background.grid(row=0, column=0)
        self.graphical_grid = []
        self._display_and_update_graphical_grid()
        self._set_bindings()

    def _display_and_update_graphical_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                val = self.grid[i][j]
                tile = Frame(self.background, bg=TILES_BG_COLOR[val], bd=1, relief='solid', height=50, width=50)
                tile.grid(row=i, column=j)
                tile.grid_propagate(False)
                label = Label(tile, text=val, fg=TILES_FG_COLOR[val], bg=TILES_BG_COLOR[val], font=TILES_FONT).grid(row=i, column=j)

    def _set_bindings(self):
        for key in ["Left", "Right", "Up", "Down"]:
            self.top.bind("<KeyPress-%s>" % key, self._key_pressed)
        self.move = ""

    def _key_pressed(self, event):
        self.move = event.keysym.lower()
        if not self.over:
            self._animate()
        else:
            if is_winning_game(self.grid):
                print("Bravo, vous avez gagné !")
            else:
                print("Désolé, vous avez perdu. Réessayez.")

    def _animate(self):
        if len(self.move) > 0:
            self.grid = move_grid(self.grid, self.move)
            self.grid = grid_add_new_tile(self.grid)
            self.over = is_game_over(self.grid)
            self._display_and_update_graphical_grid()


if __name__ == "__main__":
    game = Game()
    game.start()


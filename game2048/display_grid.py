from tkinter import *
from functools import partial
import grid_2048
import constants

width = 500
height = 500


class Game:
    def __init__(self):
        self.grid = []
        self.grid_size = 4
        self.theme = "0"
        self.over = False
        self._create_ui()

    def start(self):
        self.root.mainloop()

    def _create_ui(self):
        self.root = Tk()
        self.root.title('2048 - root')
        self.root.geometry('250x300+0+0')
        self.top = Toplevel(self.root)
        self.top.title('2048 - top')
        self.top.geometry(str(width) + 'x' + str(height) + '-250+0')
        self.top.transient(self.root)
        self._display_config()

    def _display_config(self):
        f1 = Frame(self.top).grid(row=0, column=0)

        Label(f1, text='Choose grid size').grid(row=0, column=0)
        size = IntVar(f1)
        spinbox = Spinbox(f1, textvariable=size, from_=4, to=32, increment=1)
        spinbox.config(command=partial(self._update_size, size))
        spinbox.grid(row=1, column=0)

        Label(f1, text='Choose a theme').grid(row=2, column=0)

        choices = Variable(f1, ())
        listbox = Listbox(f1, listvariable=choices, selectmode="single")
        for i in constants.THEMES.keys():
            listbox.insert('end', constants.THEMES[i]["name"])
        listbox.grid(row=3, column=0)

        button_quit = Button(f1, text='Quit', command=partial(self._quit_game))
        button_init = Button(f1, text='Init', command=partial(self._init_game, listbox))
        button_quit.grid(row=4, column=1)
        button_init.grid(row=4, column=0)

    def _display_grid(self):
        self.background = Frame(self.top, bd=1, relief='solid')
        self.background.grid(row=0, column=0)
        self.graphical_grid = []
        self._display_and_update_graphical_grid()
        self._set_bindings()

    def _update_size(self, size):
        value = size.get()
        self.grid_size = value

    def _init_game(self, listbox):
        if len(listbox.curselection()) > 0:
            self.theme = str(listbox.curselection()[0])
        self.grid = grid_2048.init_game(self.grid_size)
        self.over = False
        self._display_grid()

    def _quit_game(self):
        self.root.destroy()

    def _display_and_update_graphical_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                val = self.grid[i][j]
                tile = Frame(self.background, bg=constants.TILES_BG_COLOR[val], bd=1, relief='solid', height=height/self.grid_size, width=width/self.grid_size)
                tile.grid(row=i, column=j)
                tile.grid_propagate(False)
                text = constants.THEMES[self.theme][val]
                label = Label(tile, text=text, fg=constants.TILES_FG_COLOR[val], bg=constants.TILES_BG_COLOR[val], font=constants.TILES_FONT)
                label.grid(row=i, column=j)

    def _set_bindings(self):
        for key in ["Left", "Right", "Up", "Down"]:
            self.top.bind("<KeyPress-%s>" % key, self._key_pressed)
        self.move = ""

    def _unset_binding(self):
        for key in ["Left", "Right", "Up", "Down"]:
            self.top.unbind("<KeyPress-%s>" % key)

    def _close_game(self):
        self.message.destroy()
        self.background.destroy()

    def _key_pressed(self, event):
        self.move = event.keysym.lower()
        if not self.over:
            self._animate()
        else:
            self._unset_binding()
            self.message = Toplevel(self.root)
            self.message.title('2048 - Results')
            self.message.geometry('500x100-250+' + str(height + 100))
            self.message.transient(self.root)
            button = Button(self.message, text='OK', command=partial(self._close_game))
            if grid_2048.is_winning_game(self.grid):
                Label(self.message, text='Bravo, vous avez gagné !').grid(row=0, column=0)
            else:
                Label(self.message, text='Désolé, vous avez perdu. Réessayez.').grid(row=0, column=0)
            button.grid(row=1, column=0)

    def _animate(self):
        if len(self.move) > 0:
            self.grid = grid_2048.move_grid(self.grid, self.move)
            self.grid = grid_2048.grid_add_new_tile(self.grid)
            self.over = grid_2048.is_game_over(self.grid)
            self._display_and_update_graphical_grid()


if __name__ == "__main__":
    game = Game()
    game.start()


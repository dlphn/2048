import random

def create_grid(n=4):
    """
    Create a new game grid
    :param n: (int) the size of the grid nxn
    :return: (list) the grid as a list of lists
    """
    game_grid = []
    # Grid of size n x n
    for i in range(0, n):
        line = [' '] * n
        game_grid.append(line)
    return game_grid


def grid_add_new_tile_at_position(grid, x, y):
    val = get_value_new_tile()
    grid[x][y] = val
    return grid


def get_all_tiles(grid):
    result = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if isinstance(grid[i][j], int):
                result.append(grid[i][j])
            else:
                result.append(0)
    return result


def get_value_new_tile():
    """
    Randomly pick the value of a new tile: 2 with probability 90%, 4 with probability 10%.
    :return: (int) the random value chosen
    """
    possible_values = [2] * 9 + [4]
    rand_value = random.choice(possible_values)
    return rand_value


def get_empty_tiles_positions(grid):
    result = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not isinstance(grid[i][j], int):
                result.append((i, j))
            if grid[i][j] == 0:
                result.append((i, j))
    return result


def get_new_position(grid):
    """
    Pick a random empty position
    :param grid: (list) the game grid as a list of lists
    :return: the position (x, y)
    """
    pos = get_empty_tiles_positions(grid)
    rand = random.randint(0, len(pos) - 1)
    return pos[rand]


def grid_get_value(grid, x, y):
    if not isinstance(grid[x][y], int):
        return 0
    return grid[x][y]


def grid_add_new_tile(grid):
    """
    Pick a random available position and add a new tile 2 or 4 at that position
    :param grid: (list) the game grid as a list of lists
    :return: (list) the game grid as a list of lists
    """
    x, y = get_new_position(grid)
    new_grid = grid_add_new_tile_at_position(grid, x, y)
    return new_grid


def init_game(n=4):
    """
    Create a new game grid with 2 tiles
    :param n: (int) the size of the grid
    :return: (list) the game grid as a list of lists
    """
    grid = create_grid(n)
    grid = grid_add_new_tile(grid)
    grid = grid_add_new_tile(grid)
    return grid


def grid_to_string(grid):
    result = ""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            result += " ==="
        result += "\n"
        for j in range(len(grid[i])):
            result += "| " + str(grid[i][j]) + " "
        result += "|\n"
    for j in range(len(grid)):
        result += " ==="
    return result


def long_value(grid):
    """
    :param grid: (list)
    :return: (int) the length of the longest string in the grid
    """
    tiles = get_all_tiles(grid)
    longest = 0
    for i in range(len(tiles)):
        if len(str(tiles[i])) > longest:
            longest = len(str(tiles[i]))
    return longest


def grid_to_string_with_size(grid, n):
    result = ""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            result += " " + "=" * (n + 2)
        result += "\n"
        for j in range(len(grid[i])):
            result += "| " + str(grid[i][j]) + " " * (n - len(str(grid[i][j])) + 1)
        result += "|\n"
    for j in range(len(grid)):
        result += " " + "=" * (n + 2)
    return result


def long_value_with_theme(grid, theme):
    """
    :param grid: (list)
    :param theme: (JSON) theme chosen
    :return: (int) the length of the longest string in the grid
    """
    tiles = get_all_tiles(grid)
    longest = 0
    for i in range(len(tiles)):
        val = theme[tiles[i]]
        if len(val) > longest:
            longest = len(val)
    return longest


def grid_to_string_with_size_and_theme(grid, theme, n=4):
    """
    Display the game grid nicely
    :param grid: (list)
    :param theme: (JSON) selected theme
    :param n: (int) grid size
    :return: (string) the displayed grid
    """
    longest = long_value_with_theme(grid, theme)
    result = ""
    for i in range(n):
        for j in range(n):
            result += "=" * (longest + 1)
        result += "=\n"
        for j in range(n):
            val = theme[grid[i][j]]
            result += "|" + val + " " * (longest - len(val))
        result += "|\n"
    for j in range(n):
        result += "=" * (longest + 1)
    result += "=\n"
    return result
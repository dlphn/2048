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
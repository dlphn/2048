import random


def create_grid(size):
    game_grid = []
    for i in range(0, size):
        line = [' '] * size
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
    pos = get_empty_tiles_positions(grid)
    rand = random.randint(0, len(pos) - 1)
    return pos[rand]


def grid_get_value(grid, x, y):
    if not isinstance(grid[x][y], int):
        return 0
    return grid[x][y]


def grid_add_new_tile(grid):
    x, y = get_new_position(grid)
    new_grid = grid_add_new_tile_at_position(grid, x, y)
    return new_grid


def init_game(size):
    grid = create_grid(size)
    for i in range(2):
        grid = grid_add_new_tile(grid)
    return grid
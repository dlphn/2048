import random
import constants


""" Init and display grid """


def create_grid(n=4):
    """
    Create a new game grid
    :param n: (int) the size of the grid nxn
    :return: (list) the grid as a list of lists
    """
    game_grid = []
    # Grid of size n x n
    for i in range(0, n):
        line = [0] * n
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


def long_value_with_theme(grid, theme=constants.THEMES["0"]):
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


def grid_to_string_with_size_and_theme(grid, theme=constants.THEMES["0"], n=4):
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


""" Move tile """


def move_row_left(row):
    n = len(row)
    result = [0] * n
    p = 0
    for i in range(n):
        if row[i] > 0:
            if result[p] == 0:
                result[p] = row[i]
            elif result[p] == row[i]:
                result[p] = 2 * row[i]
                p += 1
            else:
                p += 1
                result[p] = row[i]
    return result


def move_row_right(row):
    n = len(row)
    res_left = move_row_left(row)
    result = [0] * n
    p = n - 1
    for i in range(n):
        if res_left[n-i-1] != 0:
            result[p] = res_left[n-i-1]
            p -= 1
    return result


def transform_right(grid):
    n = len(grid)
    transformed = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(grid[n - 1 - j][i])
        transformed.append(row)
    return transformed


def transform_left(grid):
    n = len(grid)
    transformed = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(grid[j][n - 1 - i])
        transformed.append(row)
    return transformed


def move_grid(grid, d):
    result = []
    if d == "up" or d == "down":
        grid = transform_right(grid)
    for row in grid:
        if d == "left" or d == "down":
            result.append(move_row_left(row))
        elif d == "right" or d == "up":
            result.append(move_row_right(row))
    if d == "up" or d == "down":
        result = transform_left(result)
    return result


""" End of game """


def is_grid_full(grid):
    empty = get_empty_tiles_positions(grid)
    return len(empty) == 0


def move_possible(grid):
    """
    Test for each possible direction if the move is allowed
    :param grid: (list)
    :return: (list) list of boole
    """
    result = []
    for direction in constants.COMMANDS_FULL:
        result.append(grid != move_grid(grid, direction))
    return result


def is_game_over(grid):
    """
    Test if the game is over : the grid is full or there is no more possible moves
    :param grid: (list)
    :return: (bool)
    """
    return is_grid_full(grid) or move_possible(grid) == [False] * len(grid)


def get_grid_tile_max(grid):
    tiles = get_all_tiles(grid)
    maxi = 0
    for i in range(len(tiles)):
        if tiles[i] > maxi:
            maxi = tiles[i]
    return maxi


def is_winning_game(grid):
    return get_grid_tile_max(grid) >= 2048


""" Dummy game """


def random_play():
    grid = init_game()
    print(grid_to_string_with_size_and_theme(grid))
    while not is_game_over(grid):
        rand_dir = random.choice(constants.COMMANDS_FULL)
        grid = move_grid(grid, rand_dir)
        grid_add_new_tile(grid)
        print(grid_to_string_with_size_and_theme(grid))
    if is_winning_game(grid):
        print("Bravo, vous avez gagné !")
    else:
        print("Désolé, vous avez perdu... Réessayez !")


# random_play()

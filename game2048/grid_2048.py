def create_grid(size):
    game_grid = []
    for i in range(0, size):
        line = [' '] * size
        game_grid.append(line)
    return game_grid

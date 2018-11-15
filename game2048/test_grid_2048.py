from game2048.grid_2048 import *
from pytest import *


def test_create_grid():
    assert create_grid(4) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]


def test_grid_add_new_tile_at_position():
    game_grid = create_grid(4)
    game_grid = grid_add_new_tile_at_position(game_grid, 1, 1)
    tiles = get_all_tiles(game_grid)
    assert 2 or 4 in tiles


def test_get_value_new_tile():
    assert get_value_new_tile() == 2 or 4


def test_get_all_tiles():
    assert get_all_tiles([[' ', 4, 8, 2], [' ', ' ', ' ', ' '], [' ', 512, 32, 64], [1024, 2048, 512, ' ']]) == [0, 4, 8, 2, 0, 0, 0, 0, 0, 512, 32, 64, 1024, 2048, 512, 0]
    assert get_all_tiles([[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]]) == [16, 4, 8, 2, 2, 4, 2, 128, 4, 512, 32, 64, 1024, 2048, 512, 2]
    assert get_all_tiles(create_grid(3)) == [0 for i in range(9)]


def test_get_empty_tiles_positions():
    assert get_empty_tiles_positions([[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]]) == [(0, 0), (0, 3), (1, 1), (3, 3)]
    assert get_empty_tiles_positions([[' ', 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]]) == [(0, 0), (0, 3), (1, 1), (3, 3)]
    assert get_empty_tiles_positions(create_grid(2)) == [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert get_empty_tiles_positions([[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]]) == []


def test_get_new_position():
    grid = [[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]]
    x, y = get_new_position(grid)
    assert(grid_get_value(grid, x, y)) == 0
    grid = [[' ', 4, 8, 2], [' ', ' ', ' ', ' '], [' ', 512, 32, 64], [1024, 2048, 512, ' ']]
    x, y = get_new_position(grid)
    assert(grid_get_value(grid, x, y)) == 0


def test_grid_add_new_tile():
    game_grid = create_grid(4)
    game_grid = grid_add_new_tile(game_grid)
    tiles = get_all_tiles(game_grid)
    assert 2 or 4 in tiles


def test_init_game():
    grid = init_game(4)
    tiles = get_all_tiles(grid)
    assert 2 or 4 in tiles
    assert len(get_empty_tiles_positions(grid)) == 14


test_create_grid()
test_grid_add_new_tile_at_position()
test_get_value_new_tile()
test_get_all_tiles()
test_get_empty_tiles_positions()
test_get_new_position()
test_grid_add_new_tile()
test_init_game()

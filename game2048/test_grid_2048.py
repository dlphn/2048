from game2048.grid_2048 import *
from pytest import *


THEMES = {
    "0": {
        "name": "Default",
        0: "",
        2: "2",
        4: "4",
        8: "8",
        16: "16",
        32: "32",
        64: "64",
        128: "128",
        256: "256",
        512: "512",
        1024: "1024",
        2048: "2048",
        4096: "4096",
        8192: "8192"
    },
    "1": {
        "name": "Chemistry",
        0: "",
        2: "H",
        4: "He",
        8: "Li",
        16: "Be",
        32: "B",
        64: "C",
        128: "N",
        256: "O",
        512: "F",
        1024: "Ne",
        2048: "Na",
        4096: "Mg",
        8192: "Al"
    },
    "2": {
        "name": "Alphabet",
        0: "",
        2: "A",
        4: "B",
        8: "C",
        16: "D",
        32: "E",
        64: "F",
        128: "G",
        256: "H",
        512: "I",
        1024: "J",
        2048: "K",
        4096: "L",
        8192: "M"
    }
}


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


def test_grid_to_string():
    a = """
 === === === ===
|   |   |   |   |
 === === === ===
|   |   |   |   |
 === === === ===
|   |   |   |   |
 === === === ===
| 2 |   |   | 2 |
 === === === ===
    """
    grid_to_string([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]]) == a


def test_grid_to_string_with_size():
    a = """
 ====== ====== ====== ======
|      |      |      |      |
 ====== ====== ====== ======
|      |      |      |      |
 ====== ====== ====== ======
|      |      |      |      |
 ====== ====== ====== ======
| 2048 |      |      | 2    |
 ====== ====== ====== ======
    """
    grid = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2048, ' ', ' ', 2]]
    grid_to_string_with_size(grid, long_value(grid)) == a


def test_long_value_with_theme():
    grid = [[2048, 16, 32, 0], [0, 4, 0, 2], [0, 0, 0, 32], [512, 1024, 0, 2]]
    assert long_value_with_theme(grid, THEMES["0"]) == 4
    assert long_value_with_theme(grid, THEMES["1"]) == 2
    assert long_value_with_theme(grid, THEMES["2"]) == 1
    grid = [[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 4096], [1024, 2048, 512, 2]]
    assert long_value_with_theme(grid, THEMES["0"]) == 4
    assert long_value_with_theme(grid, THEMES["1"]) == 2
    assert long_value_with_theme(grid, THEMES["2"]) == 1


def test_grid_to_string_with_size_and_theme():
    grid = [[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]]
    a = """
=============
|Be|He|Li|H |
=============
|H |He|H |N |
=============
|He|F |B |C |
=============
|Ne|Na|F |H |
=============
"""
    assert grid_to_string_with_size_and_theme(grid, THEMES["1"], 4) == a[1:]


test_create_grid()
test_grid_add_new_tile_at_position()
test_get_value_new_tile()
test_get_all_tiles()
test_get_empty_tiles_positions()
test_get_new_position()
test_grid_add_new_tile()
test_init_game()
test_grid_to_string()
test_grid_to_string_with_size()
test_long_value_with_theme()
test_grid_to_string_with_size_and_theme()

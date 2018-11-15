import pytest
from game2048.textual_2048 import *
from game2048.constants import COMMANDS


def test_read_player_command():
    def mock_input_return(obj):
        return 'd'
    pytest.monkeypatch.setitem('read_player_command', mock_input_return)
    move = read_player_command()
    assert move in COMMANDS


# test_read_player_command()
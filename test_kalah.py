import pytest

import kalah
import py


@pytest.fixture
def game():
    return kalah.Kalah(6 , 4)
def test_create_kalah_instance(game):
    """This is an example test. Please delete me."""
    # game = kalah.Kalah()
    assert game.status() == (4,4,4,4,4,4,0,4,4,4,4,4,4,0)


def test_illegal_hole(game):
    assert pytest.raises( IndexError, game.play ,  -1)
    assert pytest.raises(IndexError, game.play, 20)
    assert pytest.raises(IndexError, game.play, -2)
    assert pytest.raises(IndexError, game.play, -11)
    assert pytest.raises(IndexError, game.play, -12)
    assert pytest.raises(IndexError, game.play, 100)

def test_simple_move(game):
    game.play(0)
    assert game.status() == (0,5,5,5,5,4,0,4,4,4,4,4,4,0)
    game.play(7)
    assert game.status() == (0, 5, 5, 5, 5, 4, 0, 0, 5, 5, 5, 5, 4, 0)


def test_Crossing_move(game):
    game.play(4)
    assert game.status() == (4,4,4,4,0,5,1,5,5,4,4,4,4,0)
    game.play(12)
    assert game.status() == (5,5,5,4,0,5,1,5,5,4,4,4,0,1)
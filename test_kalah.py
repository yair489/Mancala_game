import pytest

import kalah
import py


@pytest.fixture
def game():
    return kalah.Kalah(6 , 4)

@pytest.fixture
def game2():
    return kalah.Kalah(6 , 9)
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



def test_Crossing_move(game):
    game.play(4)
    assert game.status() == (4,4,4,4,0,5,1,5,5,4,4,4,4,0)
    game.play(12)
    assert game.status() == (5,5,5,4,0,5,1,5,5,4,4,4,0,1)

def test_Two_simple_moves(game):
    game.play(0)
    assert game.status() == (0,5,5,5,5,4,0,4,4,4,4,4,4,0)
    game.play(7)
    assert game.status() == (0, 5, 5, 5, 5, 4, 0, 0, 5, 5, 5, 5, 4, 0)

def test_player_crosses(game):
    '''
    "1.2 Player 2 crosses":
    play
    player 1 simple ->
    player 2 simple ->
    player 1crosses ->
    player 2 crosses,
    with some moves crossing.
    '''
    game.play(0)
    assert game.status() == (0,5,5,5,5,4,0,4,4,4,4,4,4,0)
    game.play(7)
    assert game.status() == (0, 5, 5, 5, 5, 4, 0, 0, 5, 5, 5, 5, 4, 0)
    game.play(3)
    assert game.status() == (0, 5, 5, 0, 6, 5, 1, 1, 6, 5, 5, 5, 4, 0)
    game.play(12)
    assert game.status() == (1, 6, 6, 0, 6, 5, 1, 1, 6, 5, 5, 5, 0, 1)

def test_Crossing_other_store():
    '''
    "1.2 Crossing other store" Move across the other store and skip it.
Write Test. Commit, Implement. Commit. Push.

    '''
game3 = kalah.Kalah(6 , 4)
def test_empty_hole(game):
    game.play(0)
    assert game.status() == (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0)
    game.play(7)
    assert game.status() == (0, 5, 5, 5, 5, 4, 0, 0, 5, 5, 5, 5, 4, 0)
    assert pytest.raises(ValueError ,  game.play , 0)

def test_bonus_move_store(game):
    '''
    "1.3 Bonus Move player 1": Player 1 plays dropping last seed in store and gets another turn.
    '''
    game.play(2)
    assert game.status() == (4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0)
    game.play(0)
    assert game.status() == (0, 5, 1, 6, 6, 5, 1, 4, 4, 4, 4, 4, 4, 0)
    game.play(9)
    assert game.status() == (0, 5, 1, 6, 6, 5, 1, 4, 4, 0, 5, 5, 5, 1)
    game.play(8)
    assert game.status() == (0, 5, 1, 6, 6, 5, 1, 4, 0, 1, 6, 6, 6, 1)
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

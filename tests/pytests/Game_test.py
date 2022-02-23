import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from Game import Game


class TestGame:
    def test_get_winner_score(self, game):
        assert(game.get_winner_score() == 100)
        
    def test_initialize_game(self):
        assert False

    @pytest.fixture(scope='function', autouse=True)
    def game(self):
        return Game()

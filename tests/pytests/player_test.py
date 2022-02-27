import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from src.player import Player


class TestPlayer:
    """Testing Plyer class."""

    def test_get_set_cheat_rate(self, player):
        assert player.get_cheat_rate() == 1
        player.set_cheat_rate(10)
        assert player.get_cheat_rate() == 10
        player.set_cheat_rate(30)
        assert player.get_cheat_rate() == 30

    def test_add_points(self, player):
        assert player.get_total_points() == 0
        player.add_points(10)
        assert player.get_total_points() == 10
        player.add_points(18)
        assert player.get_total_points() == 28
        player.add_points(4)
        assert player.get_total_points() == 32

    def test_set_cheat_rate(self, player):
        assert player.get_total_points() == 0
        player.set_cheat_rate(2)
        player.add_points(5)
        assert player.get_total_points() == 10
        player.set_cheat_rate(10)
        player.add_points(2)
        assert player.get_total_points() == 30

    @pytest.fixture(scope="function")
    def player(self):
        return Player()

import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from lib.gui_helper import GUIHelper
from src.game import Game
from src.bot import Bot
from src.dice import Dice
from src.intelligence_low import IntelligenceLow
from src.intelligence_high import IntelligenceHigh


class TestBot:
    @pytest.mark.parametrize('execution_number', range(5))
    def test_roll_again_iq_low(self, bot_low, execution_number):
        decision = bot_low.roll_again(0, 0, 0, 0)
        assert(type(decision) is bool)

    @pytest.mark.parametrize(
        "test_param",
        [
            [0, 0, 0, 0, True],  # beginning of the game
            [87, 91, 3, 3, True],  # bot last roll
            [98, 81, 3, 3, True],  # player last roll
            [37, 29, 18, 3, False],  # optimal turn score
            [87, 79, 10, 5, True],  # max turn roll score
            [37, 29, 26, 7, False],  # finish turn
            [77, 87, 18, 3, False],  # winning score
        ],
    )
    def test_roll_again_iq_high(self, bot_high, test_param):
        res = test_param.pop()
        assert(bot_high.roll_again(*test_param) == res)

    @pytest.mark.parametrize('bot, player_total', [
        (pytest.lazy_fixture('bot_low'), 0),
        (pytest.lazy_fixture('bot_high'), 60),
        (pytest.lazy_fixture('bot_high'), 90),
        (pytest.lazy_fixture('bot_high'), 100),
        (pytest.lazy_fixture('bot_high'), 105),
    ])
    def test_play(self, bot, player_total, capsys):
        bot.play(Dice(), player_total, lambda x: x, 0)
        captured = capsys.readouterr().out  # '5\n2\n6\n'
        assert(type(captured) is str)
        elements = captured.split("\n")
        assert(len(list(filter(lambda i: i not in range(1, 7), elements))))

    @pytest.fixture(scope="function")
    def bot_low(self):
        return Bot("Computer", IntelligenceLow(None), GUIHelper())

    @pytest.fixture(scope="function")
    def bot_high(self):
        return Bot("Computer", IntelligenceHigh(Game()), GUIHelper())

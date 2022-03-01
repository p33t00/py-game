import builtins
import io
import sys
import os
from pathlib import Path
from unittest.mock import patch
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../../lib"))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../../lib/intelligence"))

from src.ui import UI
from src.bot import Bot
from src.dice import Dice
from src.game import Game
from src.player import Player
from gui_helper import GUIHelper
from intelligence import Intelligence
from intelligence_high import IntelligenceHigh
from intelligence_low import IntelligenceLow


class TestUI:
    ping = 0

    def test_do_start(self, capsys):
        ui = UI()
        sys.stdin = io.StringIO("Pete\n2")

        ui.do_start("")
        out, err = capsys.readouterr()

        assert err == ""
        expect = "Enter your name: Select Bot intelligence level:\n1. Low\n2. High\nLets Begin !\n"
        assert out == expect
        assert isinstance(ui.get_game(), Game)

        assert isinstance(ui.get_dice(), Dice)
        assert ui.get_dice().get_turn_roll_num() == 0
        assert ui.get_dice().get_turn_total_score() == 0

        assert isinstance(ui.get_bot(), Bot)
        assert isinstance(ui.get_bot().get_intelect(), Intelligence)
        assert ui.get_bot().get_name() == "Computer"
        assert ui.get_bot().get_total_points() == 0

        assert isinstance(ui.get_player(), Player)
        assert ui.get_player().get_name() == "Pete"
        assert ui.get_player().get_total_points() == 0

    def test_do_reset_bot(self, ui):
        assert(isinstance(ui.get_bot(), Bot))
        ui._UI__reset_bot()
        assert(ui.get_bot() is None)
        assert False

    def test_get_game(self, ui):
        assert(isinstance(ui.get_game(), Game))

    def test_get_dice(self, ui):
        assert(isinstance(ui.get_dice(), Dice))

    def test_get_bot(self, ui):
        assert(isinstance(ui.get_bot(), Bot))

    def test_get_player(self, ui):
        assert(isinstance(ui.get_player(), Player))

    def test_get_ghelper(self, ui):
        assert(isinstance(ui.get_ghelper(), GUIHelper))

    @pytest.mark.slow
    def test_preloop(self, capsys):
        ui = UI()
        result = Path("assets/intro.txt").read_text("UTF8") + \
            "\n\n" + \
            Path("assets/rules_n_instruct.txt").read_text("UTF8")

        ui.preloop()
        out, err = capsys.readouterr()

        assert(err == "")
        assert(out == result)

    @pytest.mark.parametrize("points", [1, 2, 3, 4, 5, 6])
    def test_roll(self, monkeypatch, capsys, ui, points):
        monkeypatch.setattr(GUIHelper, "get_picto_dice", lambda x, i: i)
        monkeypatch.setattr(Dice, "roll", lambda x: points)
        monkeypatch.setattr(UI, "do_stop", lambda x, i: print("stop"))

        ui._UI__roll()
        out, err = capsys.readouterr()

        assert(err == "")
        if points == 1:
            assert((out[-5:]).strip() == "stop")
        else:
            assert(int((out[-2:]).strip()) == points)

    @pytest.mark.slow
    def test_cheat(self, ui):
        player = ui.get_player()
        assert(player.get_cheat_rate() == 1)
        ui._UI__cheat("5")
        assert(player.get_cheat_rate() == 5)
        player.add_points(10)
        assert(player.get_total_points() == 50)

    @patch('src.ui.UI._UI__roll')
    def test_game_init_check_true(self, roll_mock, monkeypatch, ui):
        monkeypatch.setattr(UI, "_UI__get_init_bot", lambda: "Bot")
        monkeypatch.setattr(builtins, "input", lambda x: "Player1")

        ui.do_roll("")
        roll_mock.assert_called()

    def test_game_init_check_false(self, capsys):
        ui = UI()
        ui.do_roll("")
        out, err = capsys.readouterr()

        assert err == ""
        expect = "Please start the game first\n"
        assert out == expect

    @pytest.mark.parametrize("idx, result", [(1, IntelligenceLow), (2, IntelligenceHigh)])
    def test_get_init_bot(self, ui, idx, result):
        sys.stdin = io.StringIO(f"{idx}\n")
        bot = ui._UI__get_init_bot()
        assert(isinstance(bot.get_intelect(), result))

    def test_reset_bot(self, ui):
        assert(isinstance(ui.get_bot(), Bot))
        ui._UI__reset_bot()
        assert(ui.get_bot() is None)

    @pytest.mark.parametrize("player_total, result", [(90, False), (80, True)])
    def test_process_and_continue(self, monkeypatch, ui, player_total, result):
        monkeypatch.setattr(UI, "_UI__game_over_handler", lambda x, i: x)
        player = ui.get_player()
        dice = ui.get_dice()

        player.add_points(player_total)
        dice._Dice__set_turn_total_score(12)
        assert(player.get_total_points() == player_total)
        res = ui._UI__process_and_continue(player)

        assert(dice.get_turn_total_score() == 0)
        assert(player.get_total_points() == (player_total + 12))
        assert(res == result)

    @pytest.fixture(scope="function")
    def ui(self):
        ui = UI()
        sys.stdin = io.StringIO("Pete\n2")
        ui.do_start("")
        return ui

    @pytest.fixture(scope="function", autouse=True)
    def mockings(self, monkeypatch):
        monkeypatch.setattr(UI, "cls", lambda x: "")
        yield

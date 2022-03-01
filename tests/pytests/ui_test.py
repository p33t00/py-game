import builtins
import io
import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../../lib/intelligence"))

from src.ui import UI
from src.bot import Bot
from src.dice import Dice
from src.game import Game
from src.player import Player
from intelligence import Intelligence


class TestUI:
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

    def test__game_init_check_true(self, monkeypatch, capsys):
        monkeypatch.setattr(UI, "_UI__roll", lambda x: x)
        ui = UI()
        sys.stdin = io.StringIO("Pete\n2")

        ui.do_start("")
        ui.do_roll("")
        out, err = capsys.readouterr()

        assert err == ""
        expect = "Enter your name: Select Bot intelligence level:\n1. Low\n2. High\nLets Begin !\n"
        assert out == expect

    def test__game_init_check_false(self, monkeypatch, capsys):
        ui = UI()
        monkeypatch.setattr(UI, "_UI__roll", lambda x: print("inside"))

        ui.do_roll("")
        out, err = capsys.readouterr()

        assert err == ""
        expect = "Please start the game first\n"
        assert out == expect



    @pytest.mark.parametrize("player_total, result", [(90, False), (80, True)])
    def test__process_and_continue(self, monkeypatch, ui, player_total, result):
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

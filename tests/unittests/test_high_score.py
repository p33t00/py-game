"""Test HighScore module."""
import unittest
import io
import sys
import os

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from src.high_score import HighScore


class TestHighScore(unittest.TestCase):
    """Test High Score class."""

    highscore = HighScore()

    def test_store_score_in_dict(self):
        """Stores Player Name and Score in dictionary."""
        player = "Octane"
        points = 94
        return_obj = self.highscore.store_score_in_dict(player, points)
        assert type(return_obj) is dict
        self.assertEqual(return_obj[player], points)
        assert return_obj[player] == points

    def test_store_score_dict_in_file(self):
        """Stores the dictionary in file."""
        ex_player_and_score = {
            "Vivi": 106,
            "CB97": 86,
            "SpearB": 69,
        }
        temp_dict = {}
        file = self.highscore.store_score_dict_in_file(
            ex_player_and_score, "random.txt"
        )
        with open(file, "r") as read_file:
            for line in read_file:
                name, _, points = line.partition(":")
                points = int(points)
                temp_dict[name] = points
        self.assertDictEqual(ex_player_and_score, temp_dict)

    def test_read_file_should_fail(self):
        """Fails to read file."""
        filename = "should_fail.txt"
        with self.assertRaises(FileNotFoundError):
            self.highscore.all_players_and_high_scores(filename)
            self.highscore.change_name_in_file("my_name", "not_my_name", filename)
            self.highscore.count_played(filename)

    def test_sort_top_scores(self):
        """Displays top 3 score."""
        hs_dict = {
            "Killua": 100,
            "M.D.Luffy": 99,
            "Beerus": 87,
            "Gramaki": 67,
            "Vondeloma": 45,
        }
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.highscore.sort_top_scores(hs_dict, 3)
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()

        self.assertTrue("Killua" in output)
        self.assertFalse("Vondeloma" in output)

    def test_all_players_and_high_scores(self):
        """Players with their highest Score."""
        ex_dict = {
            "vivian": 120,
            "Vivi": 150,
            "Sanji": 99,
            "Jazz": 200,
            "Alluka02": 95,
            "Killua": 100,
        }
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "random1.txt")
        return_dict = self.highscore.all_players_and_high_scores(filename)
        self.assertDictEqual(ex_dict, return_dict)

    def test_change_name_in_file(self):
        """Should change a name with a new name."""
        filename = "random2.txt"
        with open(filename, "w") as f:
            f.write("Vivi:120")
        return_file = self.highscore.change_name_in_file("Vivi", "vivian", filename)
        self.assertTrue(filename.__contains__, return_file.__contains__)

    def test_count_played(self):
        """Number of games played a the Player."""
        same_dict = {"vivian": 1, "Chris": 97, "Jazz": 102}
        similar_dict = {"Vivi": 106}
        re_dict = self.highscore.count_played("random2.txt")
        self.assertDictContainsSubset(re_dict, same_dict)
        self.assertNotEqual(similar_dict, re_dict)


if __name__ == "__main__":
    unittest.main()

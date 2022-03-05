"""High Score module."""


class HighScore:
    """HighScore implementation."""

    score_dict = {}
    high_scores = {}
    played_games = {}

    def store_score_in_dict(self, player_name, player_score):
        """Store name and score of the player in a dictionary."""
        self.score_dict[player_name] = player_score
        return self.score_dict

    def store_score_dict_in_file(
        self,
        dict_of_each_player,
        filename="Score.txt"
    ):  # pylint: disable=R0201
        """Store every player attempt in Score file."""
        try:
            with open(filename, "a", encoding="UTF-8") as file:
                for name, pts in dict_of_each_player.items():
                    file.write(f"{name}:{pts}\n")
        except FileNotFoundError:
            print("File cannot be found!")
        return filename

    def all_players_and_high_scores(self, filename="Score.txt"):
        """Collect contents the players and their scores from file."""
        with open(filename, "r", encoding="UTF-8") as read_file:
            for line in read_file:
                name, _, points = line.partition(":")
                points = int(points)
                if name and points:
                    if name in self.high_scores:
                        if points > self.high_scores[name]:
                            self.high_scores[name] = points
                    else:
                        self.high_scores[name] = points
        return self.high_scores

    def display_scoreboard(self, high_scores):
        """Display Scoreboard."""
        print("  Name\t\tHigh Score  ")
        print("----------------------------")
        self.sort_top_scores(self, high_scores, 5)
        print("----------------------------")

    def sort_top_scores(self, high_scores, top_n_score: int):  # pylint: disable=R0201
        """Sort and display top_n scores."""
        for idx, (name, points) in enumerate(
            sorted(high_scores.items(), key=lambda x: -x[1])
        ):
            print(f"  {name:14s}{points}")
            print(" -------------------------- ")
            if top_n_score and idx == top_n_score - 1:
                break

    def change_name_in_file(
        self,
        old_name,
        new_name,
        filename="Score.txt"
    ):  # pylint: disable=R0201
        """Change player name to new name."""
        try:
            with open(filename, "r", encoding="UTF-8") as read_file:
                data = read_file.read()
            new_data = data.replace(old_name, new_name)
            with open(filename, "w", encoding="UTF-8") as write_file:
                write_file.write(new_data)
        except FileNotFoundError:
            print("File cannot be found!")
        return filename

    def count_played(self, filename="Score.txt"):
        """Count number of games played by the Player."""
        with open(filename, "r", encoding="UTF-8") as read_file:
            content = read_file.read()
        with open(filename, "r", encoding="UTF-8") as r_file:
            for line in r_file:
                name, _, points = line.partition(":")
                points = int(points)
                num = content.count(name)
                self.played_games[name] = num
        return self.played_games

    def display_stats(self):
        """Display Statistics."""
        max_pts = self.all_players_and_high_scores(self)
        played = self.count_played(self)
        print("  Name\t\tHigh Score\tPlayed Games  ")
        print("----------------------------------------------")
        for key, count in played.items():
            for name, pts in max_pts.items():
                if key == name:
                    print(f"  {name:14s}{pts:^14}{count:^14}  ")
            print(" ------------------------------------------")
        print("----------------------------------------------")

# stores high score of player from a Game into a file
# High score can be retrieved from file when needed
# Provides functionality to change Player's name


class HighScore:
    score_dict = {}
    filename = "Score_file.txt"
    temp_dict = {}

    def store_score_in_dict(self, player_name, player_score):
        """Store name and score of the player in a dictionary."""
        self.score_dict[player_name] = player_score
        self.store_score_dict_in_file(self)

    def store_score_dict_in_file(self):
        """Store every player attempt in Score file"""
        with open(self.filename, "a") as f:
            for name,pts in self.score_dict.items():
                f.write(f"{name}:{pts}\n")
        self.collect_all_players_and_scores(self)

    def collect_all_players_and_scores(self):
        """Collect all the players and their scores from file"""
        with open(self.filename, "r") as rf:
            for line in rf:
                name,_,points = line.partition(":")
                points = int(points)
                if name and points:
                    if name in self.temp_dict:
                        if points > self.temp_dict[name]:
                            self.temp_dict[name] = points
                    else:
                        self.temp_dict[name] = points

    def display_scoreboard(self):
        """Display Scoreboard"""
        print(f"  Name\t\tHigh Score  ")
        print("----------------------------")
        self.sort_top_scores(self.temp_dict, 5)
        print("----------------------------")

    def sort_top_scores(temp_dict, top_n_score:int):
        """Sort and display top_n scores"""
        for idx,(name,points) in enumerate(sorted(temp_dict.items(), key = lambda x : -x[1])):
            print(f"  {name:14s}{points}")
            print(" -------------------------- ")
            if top_n_score and idx == top_n_score - 1:
                    break

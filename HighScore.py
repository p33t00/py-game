# stores high score of player from a Game into a file
# High score can be retrieved from file when needed
# Provides functionality to change Player's name

from src.participant import Participant

class HighScore:
    #highest_score = 0
    score_dict = {}

    def store_info_in_dict(self):
        self.score_dict[Participant.get_name()] = int(Participant.get_total_points())

    def store_highscore_in_file(self, top_n_score = 0):
        """Store the dict into a file, only store top_n highest values."""
        with open("HighScore.txt","a") as f:
            for idx,(name,pts) in enumerate(sorted(self.score_dict.items(), key = lambda x : -x[1])):
                f.write(f"{name}:{pts}\n")
                if top_n_score and idx == top_n_score - 1:
                    break

    def display_highscore():
#        """Retrieve Name & Scores from file"""
        """Display Scoreboard"""

        try:
            print(f"  Name\t\tHigh Score  ")
            print("----------------------------")
            with open("HighScore.txt","r") as f:
                for line in f:
                    name,_,points = line.partition(":")
                    if name and points:
                        print(f"{name}\t\t{points}")
                    print(" -------------------------- ")
            print("----------------------------")
            
        except FileNotFoundError:
            return print("File not found!")

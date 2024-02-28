"""Scoreboard Module."""

import pickle  # Import the pickle module to save the game stats.
import time  # Import the time module to add a delay to the game.


class Scoreboard:
    """Scoreboard Class."""

    score = 0

    def draw(self):
        """Draws the game scoreboard."""
        stats = self.get_score()

        print("===================================")
        print("|           *Scoreboard*           |")
        print("===================================")
        print("| Player names           Win count |")
        print("===================================")
        # Sort the stats by win count.
        if stats is None:
            print("| -                      -         |")
        else:
            stats.sort(key=lambda x: x[1], reverse=True)
            for name, score in stats:
                print(f"| {name:22} {score:<9} |")
        print("===================================")
        print("\n")
        time.sleep(5)

    def save_score(self, player, score):
        """Save the scores in a binary file."""
        score_list = self.get_score()  # Get the existing scores
        if score_list is None:
            score_list = []
        else:
            score_list.append((player, score))  # Append the new player score
        pickle.dump(score_list, open("src/rpsg/scoreboard.dat", "ab"))

    def get_score(self):
        """Get the scores from the binary file."""
        try:
            with open("src/rpsg/scoreboard.dat", "rb") as infile:
                while True:
                    try:
                        score_list = pickle.load(infile)
                        return score_list
                    except EOFError:
                        break
        except FileNotFoundError:
            print("No scores found!")

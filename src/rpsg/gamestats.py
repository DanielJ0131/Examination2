"""GameStats Module."""

import time  # Import the time module to add a delay to the game.


class GameStats:
    """GameStats Class."""

    def __init__(self):
        """Init for the GameStats Class."""
        self.wincount = 0
        self.losecount = 0
        self.tiecount = 0
        self.gamecount = 0
        self.cheat = False

    def win(self):
        """Win Count function."""
        self.wincount += 1

    def lose(self):
        """Lose Count function."""
        self.losecount += 1

    def tie(self):
        """Tie Count function."""
        self.tiecount += 1

    def cheater(self):
        """Cheat Count function."""
        self.cheat = True

    def add_count(self):
        """Game Count function."""
        self.gamecount += 1

    def print_stats(self):
        """Print the game stats."""
        print("\nLatest score:")
        time.sleep(1)
        print(f"Game count: {self.gamecount}")
        time.sleep(0.5)
        print(f"Win count: {self.wincount}")
        time.sleep(0.5)
        print(f"Tie count: {self.tiecount}")
        time.sleep(0.5)
        print(f"Lose count: {self.losecount}")
        time.sleep(3)

    def reset_stats(self):
        """Reset the game stats."""
        self.wincount = 0
        self.losecount = 0
        self.tiecount = 0
        self.gamecount = 0
        self.cheat = False

    def __str__(self):
        """Return the string representation of the class."""
        return "GameStats"

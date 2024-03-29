"""Credits Module."""


class Credits:
    """Credits Class."""

    def __init__(self):
        """Initialize the Credits class."""

    def draw(self):
        """Draws the game credits and authors."""
        author1 = "Ngoc Hong (Mi)"
        author2 = "Chris Lubert"
        author3 = "Daniel Jönsson"
        print(" =================================")
        print("|           *Credits*             |")
        print(" =================================")
        print("|© HKR 2024 - All rights reserved.|")
        print(" =================================")
        print("|          Created by:            |")
        print(f"|-{author1}                  |")
        print(f"|-{author2}                    |")
        print(f"|-{author3}                  |")
        print(" =================================")
        print("Thank you for playing!")

    def __str__(self):
        """Return the name of the class."""
        return "Credits"

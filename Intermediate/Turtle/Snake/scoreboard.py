"""
scoreboard.py - Defines the Scoreboard class for the Snake Game.

This module handles displaying and updating the player's score on the screen.
It also displays the "Game Over" message when the game ends.

Requires:
    - turtle (built-in)
"""

from turtle import Turtle

# Constants for text alignment and font styling
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    """Class to manage the score display and game over message."""

    def __init__(self):
        """
        Initialize the scoreboard with a score of 0.

        Sets the position, hides the turtle, and writes the initial score.
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        """Update the score display on the screen."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Display the 'Game Over' message at the center of the screen."""
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

"""
food.py - Defines the Food class for the Snake Game.

This module creates the food object that the snake eats to grow.
The food appears at random positions on the screen and relocates upon being eaten.

Requires:
    - turtle (built-in)
    - random (built-in)
"""

from turtle import Turtle
import random

class Food(Turtle):
    """Class representing the food object in the Snake Game."""

    def __init__(self):
        """
        Initialize the food as a small blue circle that appears at a random location.

        Inherits from the Turtle class and modifies appearance and speed.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make the food smaller
        self.color("blue")
        self.speed("fastest")
        self.refresh()  # Set initial random position

    def refresh(self):
        """
        Move the food to a new random location within the game boundaries.

        Called when the snake eats the food.
        """
        random_x = random.randint(-200, 280)
        random_y = random.randint(-200, 280)
        self.goto(random_x, random_y)

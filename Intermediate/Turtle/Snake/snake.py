"""
snake.py - Defines the Snake class for the Snake Game.

This module handles the creation and control of the snake, including movement,
growth upon eating food, and directional changes based on player input.

Requires:
    - turtle (built-in)
"""

from turtle import Turtle

# Constants
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Initial snake body segments
MOVE_DISTANCE = 20                                # Distance the snake moves per step
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Class representing the snake in the Snake Game."""

    def __init__(self):
        """Initialize the snake with starting segments and define the head."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake body from predefined positions."""
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, pos):
        """
        Add a new segment to the snake at the given position.

        Args:
            pos (tuple): (x, y) coordinates for the new segment.
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        """Extend the snake by adding a new segment at the tail's position."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by shifting all segments and moving the head."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change direction to up unless the snake is currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to down unless the snake is currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to left unless the snake is currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to right unless the snake is currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

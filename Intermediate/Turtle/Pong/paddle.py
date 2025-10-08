from turtle import Turtle

class Paddle(Turtle):
    """
    A class to represent a paddle in the Pong game.

    Inherits from the Turtle class and allows vertical movement.
    Each paddle is created with a specified starting position.
    """

    def __init__(self, position):
        """
        Initialize the paddle with the given position.

        Parameters:
        - position (tuple): A tuple representing the (x, y) starting coordinates.
        """
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """
        Move the paddle upward by 20 units.
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Move the paddle downward by 20 units.
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

from turtle import Turtle

class Ball(Turtle):
    """
    A class to represent the ball in a Pong game.

    Inherits from the Turtle class. Handles movement, bouncing,
    and resetting behavior for the game ball.
    """
    
    def __init__(self):
        """Initialize the ball with shape, color, movement speed, and direction."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Move the ball by updating its x and y coordinates."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the y-direction of the ball (used when hitting top/bottom walls)."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the x-direction of the ball and increase speed slightly (used when hitting paddles)."""
        self.x_move *= -1
        self.move_speed *= 0.9  # Speed up the game gradually

    def reset_position(self):
        """
        Reset the ball to the center of the screen,
        restore original speed, and reverse direction.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

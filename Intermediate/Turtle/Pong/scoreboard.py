from turtle import Turtle

class Scoreboard(Turtle):
    """
    A class to represent the scoreboard in the Pong game.

    Inherits from the Turtle class. Tracks and displays the scores of the
    left and right players at the top of the screen.
    """

    def __init__(self):
        """
        Initialize the scoreboard with scores set to 0 and display them on screen.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clear the previous scores and update the scoreboard display.
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        """
        Increment the left player's score and update the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increment the right player's score and update the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()

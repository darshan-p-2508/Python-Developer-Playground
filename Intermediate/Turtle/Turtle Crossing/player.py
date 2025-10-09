from turtle import Turtle

# Constants for the player's starting position, move distance, and finish line
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """
    Player class represents the player character in the game.
    
    Inherits from the Turtle class to create a player object that moves
    upwards towards the finish line. The player can start at a given position,
    move up on the screen, and check if they've crossed the finish line.
    """
    
    def __init__(self):
        """
        Initialize the player by setting its shape, position, and heading.
        The player is placed at the starting position and faces upwards.
        """
        super().__init__()  # Initialize the parent Turtle class
        self.shape("turtle")  # Set the shape of the player as a turtle
        self.penup()  # Lift the pen to avoid drawing while moving
        self.go_to_start()  # Place the player at the starting position
        self.setheading(90)  # Set the turtle's heading to face upward (90 degrees)

    def go_up(self):
        """
        Move the player up the screen by a set distance.
        Called when the player presses the "Up" key.
        """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """
        Reset the player's position to the starting coordinates.
        This is typically called when the player reaches the finish line.
        """
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """
        Check if the player has crossed the finish line.
        
        Returns:
            bool: True if the player’s y-coordinate is greater than the finish line y-coordinate,
                  indicating that the player has reached the finish line.
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

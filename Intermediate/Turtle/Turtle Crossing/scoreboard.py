from turtle import Turtle

# Define font settings for displaying the score
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """
    Scoreboard class manages the display of the player's level in the game.
    
    Inherits from the Turtle class to create a scoreboard object that shows the current level.
    The scoreboard is updated each time the player advances a level and displays a game over message
    when the game ends.
    """
    
    def __init__(self):
        """
        Initializes the scoreboard by setting the starting level to 1, hiding the turtle cursor,
        and positioning the scoreboard at the top-left of the screen. The level is displayed.
        """
        super().__init__()  # Initialize the parent Turtle class
        self.level = 1  # Starting level is 1
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Lift the pen to avoid drawing while moving
        self.goto(-280, 250)  # Position the scoreboard at the top-left
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Display the level

    def update_scoreboard(self):
        """
        Clears the current level display and writes the updated level on the scoreboard.
        Called after increasing the level to reflect the new level.
        """
        self.clear()  # Clear the previous level text
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the updated level

    def increase_level(self):
        """
        Increases the player's level by 1 and updates the scoreboard to reflect the new level.
        """
        self.level += 1  # Increment the level by 1
        self.update_scoreboard()  # Update the scoreboard with the new level

    def game_over(self):
        """
        Displays the 'GAME OVER' message at the center of the screen when the game ends.
        """
        self.goto(0, 0)  # Move the cursor to the center of the screen
        self.write(f"GAME OVER", align="center", font=FONT)  # Write the 'GAME OVER' message

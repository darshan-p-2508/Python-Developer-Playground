"""
Turtle Race Game

This script simulates a turtle race where the user can bet on which turtle will win based on color. 
The race continues until one turtle crosses the finish line, and the result is displayed, showing whether 
the user won or lost based on their bet.

Features:
- User input prompts for betting on a turtle color.
- Random movement of turtles along the x-axis.
- Interactive screen with graphical feedback using the turtle module.

Modules used:
- turtle: For creating graphical turtles and setting up the screen.
- random: For generating random distances for each turtle's movement.

Game Flow:
1. The screen is set up with specific dimensions.
2. The user is prompted to enter their bet (color of turtle).
3. Turtles are created, positioned, and assigned colors.
4. The race begins and continues until a turtle crosses the finish line.
5. If the winning turtle matches the user's bet, they win; otherwise, they lose.
6. The game waits for a mouse click to close the screen after the race concludes.
"""

from turtle import Turtle, Screen
import random

# Flag to control the race status
is_race_on = True

# Set up the screen with specified width and height
screen = Screen()
screen.setup(width = 800, height = 400)

# Get user input for the turtle color they bet on
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle do you think will win the race? Enter the color: ")
# List of turtle colors to choose from
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
# List to hold all turtle objects
turtles = []

# Starting y-coordinate for positioning turtles
y_cord = -100

# Create 6 turtles, position them, and assign colors
for i in range(0, 6):
    turt = Turtle(shape = "turtle")
    turt.color(colors[i])
    turt.penup()
    turt.goto(x = -380, y = y_cord)
    y_cord += 30
    turtles.append(turt)

# Start the race if the user placed a bet
if user_bet:
    is_race_on = True

# Main race loop 
while is_race_on:
    for t in turtles:
        # Check if a turtle reached the finish line
        if t.xcor() >= 380:
            is_race_on = False
            winner = t.pencolor()
            # Check if the user’s bet matches the winning turtle
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner")
            else:
                print(f"You lose! The {winner} turtle is the winner")
        # Move the turtle a random distance
        rand_distance = random.randint(0, 10)
        t.forward(rand_distance)

# Wait for the user to click on the screen to close the window
screen.exitonclick()


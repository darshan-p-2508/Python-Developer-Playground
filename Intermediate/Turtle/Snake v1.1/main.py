"""
Snake Game using Turtle Graphics.

This script sets up and runs a simple snake game where the player controls a snake using arrow keys.
The snake eats food to grow longer and the score increases. The game ends if the snake hits the wall or itself.

Modules required:
- turtle: Built-in Python module for graphics
- snake: Custom module defining the Snake class
- food: Custom module defining the Food class
- scoreboard: Custom module to handle scoring and game over display

Controls:
- Up Arrow: Move up
- Down Arrow: Move down
- Left Arrow: Move left
- Right Arrow: Move right
"""

from turtle import Screen  # Turtle graphics screen for rendering the game
from snake import Snake    # Custom Snake class
from food import Food      # Custom Food class
from scoreboard import Scoreboard  # Custom Scoreboard class
import time                # To control game speed using sleep

# Create the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set screen dimensions
screen.bgcolor("black")              # Set background color
screen.title("Snake Game")           # Set window title
screen.tracer(0)                     # Turn off automatic screen updates

# Create game objects
snake = Snake()                      # Initialize snake
food = Food()                        # Initialize food
scoreboard = Scoreboard()            # Initialize scoreboard

# Set up key bindings for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")         # Move snake up
screen.onkey(snake.down, "Down")     # Move snake down
screen.onkey(snake.left, "Left")     # Move snake left
screen.onkey(snake.right, "Right")   # Move snake right

# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()                  # Manually update screen
    time.sleep(0.1)                  # Delay to control speed

    snake.move()                     # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()              # Reposition food
        snake.extend()              # Add new segment to snake
        scoreboard.increase_score() # Update score

    # Detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        #game_is_on = False
        #scoreboard.game_over()      # Display Game Over
        scoreboard.reset()
        time.sleep(3)
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #scoreboard.game_over()  # Display Game Over
            scoreboard.reset()
            snake.reset()

# Exit screen on click after game ends
screen.exitonclick()

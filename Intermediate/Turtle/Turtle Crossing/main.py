"""
Main game loop for the Turtle Crossing game.

This script initializes the game screen, player, car manager, and scoreboard.
It listens for key events to control the player, creates cars, moves them, and checks for collisions.
The game continues until the player collides with a car, at which point the game ends.
If the player reaches the finish line, their position is reset, the car speed increases, and the level is updated.

Modules used:
- turtle (Screen)
- player (Player)
- car_manager (CarManager)
- scoreboard (Scoreboard)
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize player, car manager, and scoreboard
player = Player()
car_manager = CarManager()
scores = Scoreboard()

# Listen for key events
screen.listen()
screen.onkey(player.go_up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Slow down the game loop for smooth gameplay
    screen.update()  # Update the screen every loop iteration

    # Create new cars and move them
    car_manager.create_car()
    car_manager.move_cars()

    # Check for collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If the car is too close to the player
            scores.game_over()  # Show game over screen
            game_is_on = False  # End the game

    # Check if player reaches the finish line
    if player.is_at_finish_line():
        player.go_to_start()  # Reset player to start position
        car_manager.level_up()  # Increase car speed/difficulty
        scores.increase_level()  # Increase the level on the scoreboard

# Wait for user click to close the screen
screen.exitonclick()

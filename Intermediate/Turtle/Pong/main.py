"""
Pong Game using the Turtle Graphics Library

This is a basic implementation of the classic Pong arcade game using Python's turtle module.
Two paddles are controlled by players: the right paddle uses the Up and Down arrow keys,
and the left paddle uses 'W' and 'S' keys. A ball bounces between the paddles and the top/bottom
edges of the screen. Players score points when the opposing player misses the ball.

Modules:
- turtle: For graphics and game loop control.
- time: For adding delay in the game loop.
- paddle.py: Defines the Paddle class for player paddles.
- ball.py: Defines the Ball class, including movement and bouncing.
- scoreboard.py: Handles player scores and display.

Author: [Your Name]
Date: [Today's Date]
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the game screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong = Ball()
scores = Scoreboard()

# Set up controls for paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong.move()

    # Bounce off top and bottom walls
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    # Bounce off paddles
    if (pong.distance(r_paddle) < 50 and pong.xcor() > 320) or \
       (pong.distance(l_paddle) < 50 and pong.xcor() < -320):
        pong.bounce_x()

    # Right player misses
    if pong.xcor() > 380:
        pong.reset_position()
        scores.l_point()

    # Left player misses
    if pong.xcor() < -380:
        pong.reset_position()
        scores.r_point()

# Exit on click
screen.exitonclick()

# Turtle documentation: "https://docs.python.org/3/library/turtle.html"
# Turtle color names: "https://trinket.io/docs/colors"
# "https://cs111.wellesley.edu/reference/colors"

from turtle import Turtle
import random

turt = Turtle()         # creating Turtle object "turt"
turt.shape("turtle")
turt.color("green")
# turt.forward(100)   # steps to move
# turt.right(90)      # mention the angle to turn

# Draw a square
for i in range(0, 4):
    turt.forward(100)
    turt.right(90)

# clear the window
turt.clear()

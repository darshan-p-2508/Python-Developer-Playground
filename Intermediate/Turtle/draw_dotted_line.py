# Turtle documentation: "https://docs.python.org/3/library/turtle.html"
# Turtle color names: "https://trinket.io/docs/colors"
# "https://cs111.wellesley.edu/reference/colors"

from turtle import Turtle
import random

turt = Turtle()         # creating Turtle object "turt"
turt.shape("turtle")
turt.color("green")

# Draw a dotted line
for i in range(0, 10):
    turt.forward(10)
    turt.penup()
    turt.forward(10)
    turt.pendown()

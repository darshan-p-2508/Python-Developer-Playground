# Turtle documentation: "https://docs.python.org/3/library/turtle.html"
# Turtle color names: "https://trinket.io/docs/colors"
# "https://cs111.wellesley.edu/reference/colors"

from turtle import Turtle
import random

turt = Turtle()         # creating Turtle object "turt"
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "LightSeaGreen", "cyan"]

# to create random pattern using fixed set of colors
directions = [0, 90, 180, 270]
turt.pensize(15)    # to set the pen size(width)
turt.speed("fastest")   # "fastest"/"fast"/"normal"/"slow"/"slowest"
turt.shape("classic")    # classic arrow shape
for i in range(200):
    turt.color(random.choice(colors))
    turt.forward(30)
    turt.setheading(random.choice(directions))   # to directly set the turtle's direction instead of right and left methods

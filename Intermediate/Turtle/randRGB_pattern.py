# Turtle documentation: "https://docs.python.org/3/library/turtle.html"
# Turtle color names: "https://trinket.io/docs/colors"
# "https://cs111.wellesley.edu/reference/colors"

import turtle as t
import random

turt = t.Turtle()         # creating Turtle object "turt"

# to create random pattern using RGB values
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)    # tuple
    return random_color

directions = [0, 90, 180, 270]
turt.pensize(15)    # to set the pen size(width)
turt.speed("fastest")   # "fastest"/"fast"/"normal"/"slow"/"slowest"
turt.shape("classic")    # classic arrow shape
for i in range(200):
    turt.color(random_color())
    turt.forward(30)
    turt.setheading(random.choice(directions))

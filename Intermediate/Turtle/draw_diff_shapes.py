# Turtle documentation: "https://docs.python.org/3/library/turtle.html"
# Turtle color names: "https://trinket.io/docs/colors"
# "https://cs111.wellesley.edu/reference/colors"

from turtle import Turtle
import random

turt = Turtle()         # creating Turtle object "turt"
turt.shape("turtle")
turt.color("green")

turt.forward(100)
# bring turt back to home (center facing east)
turt.penup()
turt.home()
turt.clear()
turt.pendown()

# to draw shaped of side 3 to 10
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "LightSeaGreen", "cyan"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        turt.forward(100)
        turt.right(angle)

for side in range(3, 11):
    turt.color(random.choice(colors))
    draw_shape(side)

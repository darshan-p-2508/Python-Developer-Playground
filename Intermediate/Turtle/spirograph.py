# Turtle documentation: "https://docs.python.org/3/library/turtle.html"
# Turtle color names: "https://trinket.io/docs/colors"
# "https://cs111.wellesley.edu/reference/colors"

import turtle as t
import random
t.colormode(255)

turt = t.Turtle()         # creating Turtle object "turt"

# to create spriograph

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)    # tuple
    return random_color

turt.speed("fastest")   # "fastest"/"fast"/"normal"/"slow"/"slowest"

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        turt.color(random_color())
        turt.circle(75)
        turt.setheading(turt.heading() + size_of_gap)
        print(turt.heading())   # .headiing() gives the orientation of the turt heading direction

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()    # exits the window on clicking the turtle window

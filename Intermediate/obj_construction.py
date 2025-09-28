# for turtle reference - "https://docs.python.org/3/library/turtle.html"

# import class from turtle module
from turtle import Turtle, Screen

# create object from the imported class
turt = Turtle()
print(turt)
turt.shape("turtle")    # to give the turt, a turtle shape
turt.color("chartreuse3")     # turns our turt into green color
# select the color you want - "https://cs111.wellesley.edu/reference/colors"
turt.forward(150)

# object attributes
my_screen = Screen()
print(my_screen.canvheight)

# object methods
my_screen.exitonclick()    # this exits the window only after click is sensed


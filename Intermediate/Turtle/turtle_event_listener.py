# Event listners - performs action based on the key/mouse clicks
from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def move_forward():
    turt.forward(10)

turt.write("Press space to move front", font=("Arial", 16, "normal"))
screen.listen()
screen.onkey(key="space", fun=move_forward) # function move_forward() as input to .onkey() function
screen.exitonclick()


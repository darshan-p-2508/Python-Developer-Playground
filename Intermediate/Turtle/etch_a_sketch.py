from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def move_forward():
    turt.forward(10)

def move_backward():
    turt.backward(10)

def turn_left():
    turt.setheading(turt.heading() + 10)

def turn_right():
    turt.setheading(turt.heading() - 10)

def clear_screen():
    turt.penup()
    turt.clear()
    turt.home()
    turt.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()


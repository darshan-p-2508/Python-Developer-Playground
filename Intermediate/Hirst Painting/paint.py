##import colorgram
##
##colors = colorgram.extract('palette.jpg', 30)
##print(colors)
##
##rgb_colors = []
##for color in colors:
##    r = color.rgb.r
##    g = color.rgb.g
##    b = color.rgb.b
##    rgb_tuple = (r, g, b)
##    rgb_colors.append(rgb_tuple)
##    
##print(rgb_colors) # once rgb_colors is printed, copy the list to below variable and comment the code so far
# as we wont have to run it everytime once the palette is decided

import turtle as t
import random

screen = t.Screen()
screen.setup(width=520, height=520)

palette = [(242, 228, 206), (211, 163, 105), (129, 93, 48), (230, 201, 127), (58, 48, 11), (85, 80, 17), (169, 143, 58), (136, 163, 191), (208, 216, 224), (50, 29, 37), (234, 238, 235), (229, 220, 224), (34, 52, 25), (103, 79, 85), (17, 18, 32), (175, 158, 167), (104, 45, 38), (184, 106, 84), (84, 102, 129), (217, 182, 171), (89, 47, 54), (109, 124, 157), (55, 76, 41), (69, 90, 55), (182, 189, 208), (203, 185, 192), (142, 118, 126), (171, 198, 208), (56, 58, 81), (133, 148, 123)]

turt = t.Turtle()
turt.penup()
turt.hideturtle()
t.colormode(255)
turt.speed("fastest")

grid_size = 10
dot_distance = 50
dot_size = 20

# Grid width/height in pixels
total_width = (grid_size - 1) * dot_distance + dot_size

start_x = -(total_width / 2)
start_y = -(total_width / 2)

turt.goto(start_x, start_y)
turt.setheading(0)

##turt.setheading(230)
##turt.forward(250)
##turt.setheading(0)

number_of_dots = 101

#to draw a dot -> Turtle hase .dot(size, color)
for dot_count in range(1, number_of_dots):
    turt.dot(20, random.choice(palette))
    turt.forward(50)

    if dot_count % 10 == 0:
        turt.setheading(90)
        turt.forward(50)
        turt.setheading(180)
        turt.forward(500)
        turt.setheading(0)

screen.exitonclick()

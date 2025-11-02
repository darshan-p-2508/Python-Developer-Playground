"""
U.S. States Game

This script creates an interactive U.S. geography quiz using the Turtle graphics module
and data from a CSV file containing all 50 U.S. states. The user is prompted to guess 
state names, which are then displayed on a blank U.S. map image upon correct entry. 
The game continues until all states are guessed or the user exits. Upon exiting, 
un-guessed states are saved to a CSV file for future study.
"""

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 | Guess the States",
        prompt="Guess a state name and enter it below. (Start with capital letter)"
    ).title()

    if answer_state == "Exit":
        #missing_states = []
        #for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

"""
The piece of code below prints the coordinates of the turtle screen
when clicked on any part within the screen
"""

# def get_mouse_click_coor(x, y):
#     """
#     Prints the (x, y) coordinates of the screen location where the user clicks.
#     Useful for finding coordinates of states on the map.
#     """
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()

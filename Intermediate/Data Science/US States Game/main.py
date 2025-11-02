"""
U.S. States Game
This script runs an interactive U.S. geography quiz using the Turtle graphics module
and data from a CSV file containing all 50 U.S. states. The user is prompted to guess 
state names, which are then displayed on a blank U.S. map image upon correct entry. 
The game continues until all states are guessed or the user exits. Upon exiting, 
unguessed states are saved to a CSV file for future study.
"""

import turtle
import pandas

# --- Setup the screen and map ---
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load blank U.S. map image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# --- Load state data from CSV ---
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  # List of all state names
guessed_states = []  # To store correctly guessed states

# --- Main Game Loop ---
while len(guessed_states) < 50:
    # Prompt user to enter a state name
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Guess a state's name (capitalize the first letter, e.g., 'Texas'):"
    )

    # If user closes the input dialog or clicks cancel
    if not answer_state:
        continue

    # Convert input to title case for consistency
    answer_state = answer_state.title()

    # Allow user to exit the game
    if answer_state == "Exit":
        # Find states that were not guessed
        missing_states = [state for state in all_states if state not in guessed_states]

        # Save missing states to a new CSV file for learning
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    # Check if the guessed state is valid and not already guessed
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Create a turtle to write the state name on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # Get the (x, y) coordinates for the guessed state from the CSV data
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())

        # Write the state's name on the map
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))


# --- (Optional) Coordinate Finder Tool ---
# Uncomment the code below to display (x, y) coordinates when clicking on the map.
# Useful for adding or adjusting coordinates in the CSV file.

# def get_mouse_click_coor(x, y):
#     """
#     Prints the (x, y) coordinates of the location where the user clicks on the screen.
#     Helpful for identifying coordinates of new states or verifying existing ones.
#     """
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Close the screen when done
# screen.exitonclick()

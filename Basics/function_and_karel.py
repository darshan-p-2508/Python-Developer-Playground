'''
def my_func():
    print("Hello")
    print("Bye")

my_func()
'''

# https://docs.python.org/3/library/functions.html
# karel the robot - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# https://peps.python.org/pep-0008/
# Indentation is used to put the lines of code into a block to let python interpreter know what the function/block contains

# go to reeborg website
# set the drop down to "Maze"
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
       turn_right()
       move()
    elif front_is_clear():
        move()
    else:
        turn_left()

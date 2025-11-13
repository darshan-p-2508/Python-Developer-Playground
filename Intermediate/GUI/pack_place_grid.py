# pack - puts components together vaguely, difficult to specify the place in the window to put the components into
# place - precise positioning
# grid - treats entire window as a grid and puts the components into rows and columns, relative to other components
# NOTE: it is mandatory to have pack/place/grid to make sure the component is on the GUI window or else that component will be ignored

'''
Explanation of Layout Managers:

Pack:
The pack() method places components sequentially in the window. It starts from the top and moves downwards (or left to right, depending on the side option). The pack() manager doesn't allow precise control over the position of the widget. It is great for simple applications where you don't need to worry too much about exact placement.

Place:
The place() method gives you complete control over the exact position of a widget. You can specify x and y coordinates to place each widget at an exact position within the window. This is useful for more custom layouts but requires you to manage the positioning of every component manually.

Grid:
The grid() method treats the window as a table, dividing it into rows and columns. Widgets are placed in a specific row and column. This allows you to create more structured layouts (like forms or tables) where components align neatly in rows and columns. You can control the widget’s position and also adjust its spanning across multiple rows or columns.

Important Note:
You cannot mix layout managers (i.e., using pack, place, and grid in the same window). Each window should use only one layout manager. If you try to mix them, you will get an error or unexpected behavior.
'''

from tkinter import *

# Function to update the label text based on user input from the Entry widget
def button_clicked():
    new_text = input.get()  # Get text from Entry widget
    my_label.config(text=new_text)  # Update the text of the label with the new input
    print("You've clicked the button")  # Print a message to the console

# ---- Window 1: Using pack layout manager ----
# In this example, we will use the 'pack' manager which places the components one after another
window1 = Tk()
window1.title("Pack Layout Example")
window1.minsize(width=500, height=300)
window1.config(padx=20, pady=20)  # Padding for the window

# Create a Label and update its text
my_label = Label(window1, text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")  # Change the text of the label
my_label.pack()  # Add the label to the window using the pack manager

# Create an Entry widget for user input
input = Entry(window1, width=25)
input.pack()  # Place the Entry widget in the window using pack

# Create a Button widget that triggers the 'button_clicked' function
button = Button(window1, text="Click here", command=button_clicked)
button.pack()  # Place the Button widget in the window using pack

# Start the first window
window1.mainloop()


# ---- Window 2: Using place layout manager ----
# In this example, we use the 'place' manager which allows us to set exact x, y coordinates for the widgets
window2 = Tk()
window2.title("Place Layout Example")
window2.minsize(width=500, height=300)
window2.config(padx=20, pady=20)

# Create a Label and update its text
my_label = Label(window2, text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")  # Change the text of the label
my_label.place(x=0, y=0)  # Place the label at coordinates (0, 0)

# Create an Entry widget for user input
input = Entry(window2, width=25)
input.place(x=100, y=100)  # Place the Entry widget at position (100, 100)

# Create a Button widget that triggers the 'button_clicked' function
button = Button(window2, text="Click here", command=button_clicked)
button.place(x=200, y=200)  # Place the Button widget at position (200, 200)

# Start the second window
window2.mainloop()


# ---- Window 3: Using grid layout manager ----
# In this example, we use the 'grid' manager which divides the window into rows and columns
window3 = Tk()
window3.title("Grid Layout Example")
window3.minsize(width=500, height=300)
window3.config(padx=20, pady=20)

# Create a Label and update its text
my_label = Label(window3, text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")  # Change the text of the label
my_label.grid(column=0, row=0)  # Position the label at grid position (0, 0)

# Create an Entry widget for user input
input = Entry(window3, width=25)
input.grid(column=2, row=2)  # Position the Entry widget at grid position (2, 2)

# Create a Button widget that triggers the 'button_clicked' function
button = Button(window3, text="Click here", command=button_clicked)
button.grid(column=3, row=3)  # Position the Button widget at grid position (3, 3)

# Start the third window
window3.mainloop()


# ---- Window 4: Mixed grid layout example ----
# Here, we mix different widgets with the grid layout to demonstrate how they align with rows and columns
window4 = Tk()
window4.title("Mixed Grid Layout Example")
window4.minsize(width=500, height=300)
window4.config(padx=20, pady=20)

# Create a Label and update its text
my_label = Label(window4, text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)  # Position label in the first column of the first row

# Create an Entry widget for user input
input = Entry(window4, width=25)
input.grid(column=3, row=2)  # Position Entry widget in the third column of the second row

# Create a new Button widget
new_button = Button(window4, text="New Button")
new_button.grid(column=2, row=0)  # Position new_button in the second column of the first row

# Create another Button widget that triggers the 'button_clicked' function
button = Button(window4, text="Click here", command=button_clicked)
button.grid(column=1, row=1)  # Position button in the second column of the second row
button.config(padx=10, pady=10)  # Add padding to the button for spacing

# Start the fourth window
window4.mainloop()

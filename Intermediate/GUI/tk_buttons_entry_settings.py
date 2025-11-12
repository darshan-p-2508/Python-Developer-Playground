# https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm
# tkinter has a bunch of layout managers that define how to position each of the widgets in your GUI program
# Efficient way to import all classes of tkinter
from tkinter import *

# Create the main window object (root window) for the GUI application
window = Tk()
window.title("My first GUI Program")  # Title of the window
window.minsize(width=500, height=300)  # Set minimum size for the window

# Label Widget - A simple text widget to display static text
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()  # Use the pack layout manager to add the label to the window

# Changing the text of the label using different methods
my_label["text"] = "New Text"  # Alternative method to change the text
my_label.config(text="New Text")  # Another alternative using config()

# Entry Widget - A simple text input field for user input
input = Entry(width=25)  # Create an Entry widget with a specified width
input.pack()  # Add Entry widget to the window using the pack manager

# Get the current text value from the Entry widget (but not used here)
input.get()

# Button Widget - A clickable button that triggers an action when clicked
def button_clicked():
    """
    Function that gets called when the button is clicked.
    It updates the label text with the input from the Entry widget.
    """
    new_text = input.get()  # Get text from Entry widget
    my_label.config(text=new_text)  # Update the text of the label with the new input
    print("You've clicked the button")  # Print a message to the console

button = Button(text="Click here", command=button_clicked)  # Create Button and link the function
button.pack()  # Add the button to the window using pack manager

# Entry Widget - Again, creating an Entry field, this time with initial text
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")  # Insert some initial text
print(entry.get())  # Retrieve and print the current text value in the entry field
entry.pack()  # Add this Entry widget to the window

# Text Widget - A multi-line text area for user input
text = Text(height=5, width=30)  # Create a Text widget with specified dimensions (rows and columns)
text.focus()  # Set focus to the Text widget so the cursor is automatically placed inside it
text.insert(END, "Example of multi-line text entry.")  # Insert some initial text into the Text widget
print(text.get("1.0", END))  # Retrieve the entire content of the Text widget, starting from line 1, char 0
text.pack()  # Add the Text widget to the window

# Spinbox Widget - A widget with a range of values that allows the user to select one
def spinbox_used():
    """
    Function that gets called whenever the user interacts with the spinbox.
    It prints the current value of the spinbox.
    """
    print(spinbox.get())  # Get the current selected value of the spinbox

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)  # Create a Spinbox widget with a range from 0 to 10
spinbox.pack()  # Add the Spinbox to the window

# Scale Widget - A slider that lets the user choose a value within a given range
def scale_used(value):
    """
    Function that gets called whenever the slider is adjusted.
    It prints the current value of the scale.
    """
    print(value)  # Print the current value of the scale

scale = Scale(from_=0, to=100, command=scale_used)  # Create a Scale widget with a range from 0 to 100
scale.pack()  # Add the Scale widget to the window

# Checkbutton Widget - A checkbox that can be toggled on or off
def checkbutton_used():
    """
    Function that gets called when the state of the checkbutton changes.
    It prints 1 if checked, otherwise 0.
    """
    print(checked_state.get())  # Print the state of the checkbutton (0 = unchecked, 1 = checked)

# Variable to hold the state of the checkbutton (0 = unchecked, 1 = checked)
checked_state = IntVar()

# Create the Checkbutton widget and link it to the checked_state variable
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()  # Add the Checkbutton widget to the window

# Radiobutton Widget - A set of radio buttons that allows only one option to be selected at a time
def radio_used():
    """
    Function that gets called whenever the user selects a radio button.
    It prints the value associated with the selected radio button.
    """
    print(radio_state.get())  # Print the value of the selected radio button

# Variable to hold the value of the selected radio button (1 or 2)
radio_state = IntVar()

# Create two Radiobutton widgets with values 1 and 2
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()  # Add the first radio button to the window
radiobutton2.pack()  # Add the second radio button to the window

# Listbox Widget - A list of selectable options (with multiple items)
def listbox_used(event):
    """
    Function that gets called when the user selects an item from the listbox.
    It prints the selected item from the listbox.
    """
    print(listbox.get(listbox.curselection()))  # Get the current selection from the listbox and print it

# Create a Listbox widget and populate it with fruit names
listbox = Listbox(height=4)  # Create a Listbox with a height of 4 lines
fruits = ["Apple", "Pear", "Orange", "Banana"]  # List of fruits to populate the Listbox
for item in fruits:
    listbox.insert(fruits.index(item), item)  # Insert each fruit into the Listbox

# Bind an event to the Listbox, calling the listbox_used function when an item is selected
listbox.bind("<<ListboxSelect>>", listbox_used)

listbox.pack()  # Add the Listbox widget to the window

# Main loop to keep the window open and respond to user actions
window.mainloop()

'''
Key Concepts:
Widgets: All the components in your GUI such as Label, Button, Entry, etc., are widgets that serve specific purposes.
Layout Managers: These determine how widgets are arranged in the window. In this code, pack() is used, which places widgets one after another in the available space.
Widget Parameters: Each widget can have various parameters (like width, height, font, value, etc.) that determine its appearance and behavior.
Command: This is used to bind a function to an event like a button click, slider movement, etc.
Variable types (IntVar, StringVar): These are special variable types in Tkinter that allow the widget to automatically update and communicate changes to other parts of the GUI.
Event Binding: For widgets like Listbox, we use bind to attach an event handler function that reacts when a user interacts with the widget.
'''

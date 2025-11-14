"""
Miles to Kilometers Converter GUI

This program creates a simple graphical user interface (GUI) using Tkinter 
that converts miles to kilometers. The user can enter a value in miles, 
click the "Calculate" button, and see the corresponding value in kilometers.

Author: Darshan P
"""

from tkinter import *  # Import all classes and functions from tkinter

def miles_to_kms():
    """Convert miles entered by the user into kilometers and display the result."""
    miles = float(miles_input.get())   # Get the value from the input field and convert to float
    km = miles * 1.60934               # Convert miles to kilometers
    kms_result_label.config(text=f"{km:.2f}")  # Update the label with the result, formatted to 2 decimals

# -------------------- UI SETUP -------------------- #
window = Tk()  # Create the main application window
window.title("Miles to Kilometers Converter")  # Set the window title
window.config(padx=20, pady=20)  # Add padding around the window for better layout

# Entry widget for user input (miles)
miles_input = Entry(width=7)  # Create an entry box with width 7 characters
miles_input.grid(column=1, row=0)  # Place the entry box in the grid layout

# Label showing "Miles" next to input box
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)  # Place in the grid layout

# Label showing "is equal to" text
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Label to display conversion result (starts at 0)
kms_result_label = Label(text="0")
kms_result_label.grid(column=1, row=1)

# Label showing "km" next to result
kms_label = Label(text="km")
kms_label.grid(column=2, row=1)

# Button to trigger the conversion function
calculate_button = Button(text="Calculate", command=miles_to_kms)
calculate_button.grid(column=1, row=2)

# Keep the window open and responsive
window.mainloop()

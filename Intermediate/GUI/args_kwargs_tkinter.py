import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left") # packs the label into the window using paker method

# --- Keyword Arguments Example ---
'''
def my_function(a, b, c):
    #Do this with a
    #then do this with b
    #finally do this with c
    pass

my_function(c=3, a=1, b=2)
'''

# --- Arguments with Default Values ---
'''
def my_function(a=1, b=2, c=3):
    #Do this with a
    #then do this with b
    #finally do this with c

my_function()

# if we say:
my_function(b=5) # Updates only b to 5; others use default values
'''

# --- Unlimited Arguments (*args) ---
'''
# Instead of manually defining all parameters:
def add(n1, n2):
    return n1 + n2

add(n1=5, n2=3)

# We can use *args for unlimited positional arguments:
def add(*args):
    print("1st element is: " + str(args[0]))
    print(sum(args))

add(1, 2, 3, 4, 5, 6, 7, 8, 9)
# *args collects arguments into a tuple
'''

# --- Many Keyword Arguments (**kwargs) ---
'''
# **kwargs packs keyword arguments into a dictionary
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    # to access one element
    print(kwargs["add"])
    # Safely access dictionary elements
    add_value = kwargs.get("add", 0)
    multiply_value = kwargs.get("multiply", 1)

    n += add_value
    n *= multiply_value
    print(n)

calculate(2, add=3, multiply=5)
'''

# Tkinter = tk commands (from other language) converted to kwargs
# --- Tkinter & **kwargs Example (Car classes) ---
'''
class Car1:
    def __init__(self, **kw):
        # Using [] can raise KeyError if the key is missing
        self.make = kw["make"]
        self.model = kw["model"]
        
class Car2:
    def __init__(self, **kw):
        # .get() returns None if the key is not found
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car1 = Car1(make="Nissan", model="GT-R")
my_car2 = Car2(make="BMW")
print(my_car1.make)
print(my_car1.model)
print(my_car2.make)
print(my_car2.model)
'''
# Explanation:
# Tkinter widgets (like Label, Button, etc.) internally use **kwargs to handle many configuration options.

# keeps the window open
window.mainloop()

def greet():
    print("Hello")
    print("How are you doing today?")

greet()

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Jack")

# parameter is the name of the data that is being passed to the function
# in this case it is name in the function greet_with_name()

# argument is the value that is being passed to the funtion when it is being called
# in this case it is "Jack"

def greet_with(name, loc):
    print(f"Hello {name}")
    print(f"Your location - {loc}, will face a light shower, carry an umbrella")

greet_with("John", "Bangalore")

# we can switch the order of the arguments by doing the following:
# keyword arguments (kwarg)
greet_with(loc = "Bangalore", name = "Jill")

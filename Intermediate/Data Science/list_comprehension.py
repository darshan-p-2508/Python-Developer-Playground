# Original list of numbers
numbers = [1, 2, 3]
# Create an empty list to store new values
new_list = []

# 'list' is a built-in keyword in Python.
# Using 'list' as a variable name hides the built-in type 'list'.
# use 'numbers' or any other variable name instead.
for n in numbers:
    add_1 = n + 1  # Adds 1 to each element
    new_list.append(add_1)  # Appends the result to new_list
print("New list using for-loop:", new_list)

# -------------------------------
# LIST COMPREHENSION (Intermediate)
# -------------------------------

# A more compact way to achieve the same result:
# Syntax: [expression for item in iterable]
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print("New list using list comprehension:", new_list)

# -------------------------------
# STRING TO LIST USING COMPREHENSION
# -------------------------------

name = "Tony Stark"

# This creates a list of individual characters from the string
new_name = [c for c in name]
print("Characters in name:", new_name)

# -------------------------------
# USING RANGE WITH COMPREHENSION
# -------------------------------

# Example: multiply each number in range(1, 6) by 2
eg_list = [i * 2 for i in range(1, 6)]
print("Doubled numbers from 1 to 5:", eg_list)

# -------------------------------
# CONDITIONAL LIST COMPREHENSION (Filter Example)
# -------------------------------

names = ["Alexa", "Beth", "Dan", "Sam", "John", "Christopher"]

# Filters names with 4 or fewer characters
new_names = [nm for nm in names if len(nm) <= 4]
print("Names with <= 4 letters:", new_names)

# -------------------------------
# CONDITIONAL LIST COMPREHENSION (Transformation Example)
# -------------------------------

# Converts names with more than 4 characters to uppercase
upper_case_names = [name.upper() for name in names if len(name) > 4]
print("Names with > 4 letters (uppercased):", upper_case_names)

# ----------ADVANCED LIST COMPREHENSION----------
# -------------------------------------------
# Inline IF–ELSE inside list comprehension
# -------------------------------------------

# Syntax: [<true_expr> if <condition> else <false_expr> for <var> in <iterable>]
# Unlike 'if' filters, this version always adds an element — either true_expr or false_expr.
numbers = [1, 2, 3, 4, 5, 6]

# Replace odd numbers with 0, keep even numbers as-is
even_or_zero = [n if n % 2 == 0 else 0 for n in numbers]
print("Even numbers kept, odd replaced with 0:", even_or_zero)
# Output: [0, 2, 0, 4, 0, 6]

# -------------------------------------------
# Multiple 'for' loops (nested iteration)
# -------------------------------------------

# You can include multiple 'for' clauses in one comprehension.
# This creates a Cartesian product (like nested loops).
colors = ["red", "green", "blue"]
objects = ["car", "bike"]

# Combine each color with each object
combinations = [f"{c} {o}" for c in colors for o in objects]
print("Color-object combinations:", combinations)
# Output: ['red car', 'red bike', 'green car', 'green bike', 'blue car', 'blue bike']

# -------------------------------------------
# Nested list comprehensions (2D → 1D)
# -------------------------------------------

# Flattening a 2D list into a single list
matrix = [[1, 2, 3], [4, 5, 6]]

# Traditional approach:
# flattened = []
# for row in matrix:
#     for num in row:
#         flattened.append(num)

# List comprehension version:
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)
# Output: [1, 2, 3, 4, 5, 6]

# -------------------------------------------
# Nested list comprehension (creating 2D structures)
# -------------------------------------------

# Create a 3x3 matrix using list comprehension
matrix_2d = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("3x3 multiplication matrix:", matrix_2d)
# Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# -------------------------------------------
# Applying functions inside comprehensions
# -------------------------------------------

# Using built-in or user-defined functions in list comprehensions
def square(num):
    return num ** 2

# Apply function to each item
squares = [square(n) for n in range(1, 6)]
print("Squares using function call:", squares)
# Output: [1, 4, 9, 16, 25]

# -------------------------------------------
# Using enumerate() in comprehensions
# -------------------------------------------

# enumerate() gives both index and value
names = ["Alice", "Bob", "Charlie"]

indexed_names = [f"{i}: {nm}" for i, nm in enumerate(names)]
print("Indexed names:", indexed_names)
# Output: ['0: Alice', '1: Bob', '2: Charlie']

# -------------------------------------------
# Conditional with multiple conditions (compound filters)
# -------------------------------------------

# Filter names starting with 'A' and with length > 3
filtered_names = [nm for nm in names if nm.startswith("A") and len(nm) > 3]
print("Filtered names (start with A, len > 3):", filtered_names)
# Output: ['Alice']

# -------------------------------------------
# Nested inline IF–ELSE with transformation
# -------------------------------------------

# Assign different labels to numbers based on their value
labels = [
    "Even" if n % 2 == 0 else "Odd" if n % 3 == 0 else "Prime candidate"
    for n in range(1, 10)
]
print("Number labels:", labels)
# Output: ['Prime candidate', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Prime candidate', 'Even', 'Odd']

# -------------------------------------------
# Flattening and transforming simultaneously
# -------------------------------------------

# Add 10 to each element while flattening a 2D list
matrix = [[1, 2, 3], [4, 5, 6]]
transformed_flat = [num + 10 for row in matrix for num in row]
print("Flattened and incremented:", transformed_flat)
# Output: [11, 12, 13, 14, 15, 16]

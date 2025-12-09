"""
This file shows examples of catching many common Python exceptions,
with explanations written directly inside the code.
"""

# ---------------------------------------------------------
# 1. ZeroDivisionError
# Raised when dividing a number by zero.
# ---------------------------------------------------------
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError caught:", e)


# ---------------------------------------------------------
# 2. ValueError
# Raised when a function receives an argument of the right type but wrong value.
# Example: converting letters to int.
# ---------------------------------------------------------
try:
    num = int("abc")
except ValueError as e:
    print("ValueError caught:", e)


# ---------------------------------------------------------
# 3. TypeError
# Raised when an operation is applied to an inappropriate type.
# Example: adding a string to an integer.
# ---------------------------------------------------------
try:
    value = 5 + "hello"
except TypeError as e:
    print("TypeError caught:", e)


# ---------------------------------------------------------
# 4. IndexError
# Raised when accessing a list index that does not exist.
# ---------------------------------------------------------
try:
    arr = [1, 2, 3]
    item = arr[5]
except IndexError as e:
    print("IndexError caught:", e)


# ---------------------------------------------------------
# 5. KeyError
# Raised when a dictionary key is not found.
# ---------------------------------------------------------
try:
    data = {"name": "John"}
    age = data["age"]
except KeyError as e:
    print("KeyError caught:", e)


# ---------------------------------------------------------
# 6. FileNotFoundError
# Happens when trying to open a file that doesn't exist.
# ---------------------------------------------------------
try:
    with open("missing_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print("FileNotFoundError caught:", e)


# ---------------------------------------------------------
# 7. PermissionError
# Happens when a file exists but you don't have rights to read/write.
# ---------------------------------------------------------
try:
    with open("/root/secret.txt", "r") as f:
        print(f.read())
except PermissionError as e:
    print("PermissionError caught:", e)


# ---------------------------------------------------------
# 8. AttributeError
# Happens when calling a method that doesn't exist on an object.
# ---------------------------------------------------------
try:
    x = 10
    x.append(5)  # integers have no append()
except AttributeError as e:
    print("AttributeError caught:", e)


# ---------------------------------------------------------
# 9. ImportError / ModuleNotFoundError
# Happens when importing an invalid module.
# ---------------------------------------------------------
try:
    import does_not_exist
except ModuleNotFoundError as e:
    print("ModuleNotFoundError caught:", e)


# ---------------------------------------------------------
# 10. NameError
# Happens when using a variable that was never defined.
# ---------------------------------------------------------
try:
    print(unknown_variable)
except NameError as e:
    print("NameError caught:", e)


# ---------------------------------------------------------
# 11. RuntimeError
# A generic runtime error. Often thrown manually or by recursion.
# ---------------------------------------------------------
try:
    import sys
    sys.setrecursionlimit(5)

    def recurse():
        recurse()

    recurse()
except RuntimeError as e:
    print("RuntimeError caught:", e)


# ---------------------------------------------------------
# 12. MemoryError (hard to force; simulated example)
# Raised when Python runs out of memory.
# We simulate catching it without actually crashing RAM.
# ---------------------------------------------------------
try:
    # Attempt to create a huge list (commented to avoid crash)
    # big_list = [0] * (10**20)
    raise MemoryError("Simulated for demo")
except MemoryError as e:
    print("MemoryError caught:", e)


# ---------------------------------------------------------
# 13. TimeoutError (often from networking or multiprocessing)
# ---------------------------------------------------------
try:
    raise TimeoutError("Simulated timeout")
except TimeoutError as e:
    print("TimeoutError caught:", e)


# ---------------------------------------------------------
# 14. OSError
# Base class for system-related errors. Many file errors subclass this.
# ---------------------------------------------------------
try:
    import os
    os.remove("/path/that/does/not/exist")
except OSError as e:
    print("OSError caught:", e)


# ---------------------------------------------------------
# 15. Catch ALL Exceptions (Not recommended unless necessary)
# Useful for logging, debugging, or preventing crashes.
# ---------------------------------------------------------
try:
    risky_operation = 10 / 0
except Exception as e:  # catches ANY exception type
    print("General Exception caught:", e)

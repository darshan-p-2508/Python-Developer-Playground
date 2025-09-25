try:
    age = int(input("How old are you? "))
except ValueError:
    print("The input should be int type, please enter the integer value.")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at the age of {age}.")
else:
    print("You can  not drive yet. As you are not 18 yet.")



words_per_page = 0 # can delete this line to avoid any warnings
pages = int(input("Number of Pages: "))
words_per_page == int(input("Number of words per page: "))
total_words = pages * words_per_page
# using print function to check the error
print(f"Pages = {pages}")
print(f"Words per page = {words_per_page}")
print(total_words)
# the actual error is we have used the "==" (comparator) instead of "=" (assignment) operator
# which doesn't assigns the user input instead sets true or false and leaves it at there, while
# the value is words_per_page is still 0

################################################
# use debugger to fix this code below

# place this function in math.py file
def add(n1, n2):
    return n1 + n2
# place this code below in random.py file
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# solution: indent the "blist.append(new_item)" to put it inside the scope of the for loop
################################################

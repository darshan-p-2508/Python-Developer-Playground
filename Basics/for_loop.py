fruits = ["Apple", "Orange", "Banana", "Pear"]
for i in fruits:
    print(i)

# i = iterator to access each elements in the fruits list

student_score = [180, 124, 165, 173, 189, 169, 146]
print("Sum of the list elements using built-in method is: " + str(sum(student_score)))

# using for loop
tot = 0
for score in student_score:
    tot += score
print("Sum of the list elements using for loop: " + str(tot))

# to find the max of the list
max_ele = 0
for ss in student_score:
    if max_ele < ss:
        max_ele = ss
print("Max element in the list using built-in function: " + str(max(student_score)))
print("Max element in the list using for loop: " + str(max_ele))

# for loop with range()
'''
for number in range(a, b):
    print(number)
'''

for num in range(1, 11):
    print(num)
for numb in range(1, 11, 3): # steps by 3
    print(numb)

tota = 0
for numbe in range(1, 101):
    tota += numbe
print("Sum of 1 to 100 is: " + str(tota))

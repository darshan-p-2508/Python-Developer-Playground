'''
numbers = [1, 2, 3]
new_list = []
for n in list:
	add_1 = n + 1
	new_list.append(add_1)
'''

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Tony Start"
new_name = [c for c in name]
print(new_name)

eg_list = [i*2 for i in range(1, 6)]
print(eg_list)

# conditional list comprehension
names = ["Alexa", "Beth", "Dan", "Sam", "John", "Christopher"]
new_names = [nm for nm in names if (len(nm) <= 4)]
print(new_names)

upper_case_names = [name.upper() for name in names if (len(name) > 4)]
print(upper_case_names)

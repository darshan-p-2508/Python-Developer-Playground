import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
           ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

print("Welcome to the Password Generator project!")
number_of_letters = int(input("How many letters would you like to have in your Password: "))
number_of_symbols = int(input("How many symbols would you like to have in your Password: "))
number_of_numbers = int(input("How many numbers would you like to have in your Password: "))

# this creates the password in sequence = letters_symbols_numbers, always
'''
password = ""
for l in range(0, number_of_letters):
    password += random.choice(letters)
    
for s in range(0, number_of_symbols):
    password += random.choice(symbols)

for n in range(0, number_of_numbers):
    password += random.choice(numbers)

print(password)
'''

# here we make the password more harder, by jumbling the selected characters
password_list = []
for i in range(0, number_of_letters):
    password_list.append(random.choice(letters))
    
for i in range(0, number_of_symbols):
    password_list.append(random.choice(symbols))

for i in range(0, number_of_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)   # shuffles the elements of the list
final_password = ""
for char in password_list:
    final_password += char

print(f"Your password is: {final_password}")

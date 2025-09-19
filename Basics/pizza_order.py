print("Welcome to Python Pizza Deliveries!")
size = input("What pizza size do you prefer? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S" or size == "s":
    bill = 25
elif size == "M" or size == "m":
    bill = 45
elif size == "L" or size == "l":
    bill = 60
else:
    print("Wrong input!!! Try again.")

if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        bill += 3
    else:
        bill += 5

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 5

print(f"Your total bill to be payed is ${bill}.")


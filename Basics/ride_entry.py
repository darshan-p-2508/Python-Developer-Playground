print("Welcome to the ride!")
height = int(input("Please enter your height (in cm): "))
bill = 0

if height >= 120:
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 5
        print("Ticket price for children is $5.")
    elif age <= 18:
        bill = 7
        print("Ticket price for teen is $7.")
    # elif 45 <= age <= 65:
    # this also works
    elif age >= 50 and age <= 65:
            print("You have earned a free ride!")
    else:
        bill = 12
        print("Ticket price for adult is $12.")

    want_photo = input("Do you want to have a photo while on the ride? Type y/Y for Yes and n/N for No.")
    if want_photo == "y" or want_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
    


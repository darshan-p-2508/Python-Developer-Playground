print("Welcome to tip calculator!")
bill_amount = int(input("What is the bill amount? "))
tip = int(input("What percent of the bill amout would you like to tip? "))
total_tip = tip / bill_amount * 100
total_amount = round((total_tip + bill_amount), 2)
number_of_people = int(input("How many people should the bill amount be split to? "))
per_person_amount = round((total_amount / number_of_people), 2)
print(f"The total amount to be paid is: ${total_amount}\nEach person would have to pay: ${per_person_amount}")

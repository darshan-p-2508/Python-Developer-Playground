import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanual"]

credit_card_of = random.randint(0, len(friends))
payee = friends[credit_card_of]
print(f"{payee} is the chosen one.\nOthers enjoy the food.")

# to directly pick the names from the list we can use randome.choice() method
print(random.choice(friends) + " would pay the bill today.")

# Nested List
hatch_back  = ["Maruti Swift", "Hyundai i20", "Tata Tiago", "Maruti WagonR", "Tata Altroz", "Renault Kwid"]
sedan = ["Maruti Suzuki Dzire", "Honda Amaze", "Hyundai Aura", "Tata Tigor", "Honda City", "Skoda Slavia"]
cars = [hatch_back, sedan]    #we got 2 lists inside one list

print(cars)

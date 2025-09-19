import random

print(random.randint(1, 9))

random_0_to_1 = random.random()
print(random_0_to_1)
# prints only the FLOAT number between the range of 0 to 1
# it can print 0.0 but never 1.0 i.e., this method excludes the upper bound

random_float = random.uniform(1, 10)
print(random_float)
# prints the random FLOAT number between the range of 1 to 10
# it includes both the limits specified

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

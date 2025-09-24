scope_enemies = 1
def decrease_enemies():
    global scope_enemies   # Uncomment this to avoid UnboundLocalError
    # We need to specify to the interpreter that we are accessing the global variable
    # Otherwise, it thinks the "scope_enemies" variable inside the function is local,
    # and since it's referenced before assignment, an error occurs
    scope_enemies -= 1
    print(f"Enemies inside the function: {scope_enemies}")  # output = 0

print(f"Enemies outside the function: {scope_enemies}")    # output = 1
decrease_enemies()




# Local scopes:
def drink_potion():
    potion_strength = 10
    print(f"Potion strength = {potion_strength}")  # this runs normally
drink_potion()
# print(f"Potion strength = {potion_strength}")  # Uncommenting this will cause NameError because potion_strength is local



# Global scope: available to all functions (inside and outside)
player_health = 75
def drink_potion():
    potion_strength = 10
    print(f"Player_health = {player_health}")  # accessed the variable normally since it is in global scope
    print(f"Potion strength = {potion_strength}")  # this runs normally
drink_potion()
# print(f"Potion strength = {potion_strength}")  # Uncommenting this produces NameError
print(f"Player_health = {player_health}")  # accessible globally



# Name scope:
player_health = 75
def game():
    def drink_potion():
        potion_strength = 10
        print(f"Player_health = {player_health}")  
        print(f"Potion strength = {potion_strength}")
    drink_potion()  # This is the correct scope to call the nested function
    # print(f"Potion strength = {potion_strength}")  # Uncommenting this will produce NameError as potion_strength is local to drink_potion()
    print(f"Player_health = {player_health}")

game()



# Python has no block scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)  # prints "Skeleton" as new_enemy is not restricted by any block scope

# If the if block was inside a function, then the new_enemy variable would only be available to that function



game_level1 = 2
enemies1 = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""  # Initialize the variable to avoid warnings when using the same variable name as argument
    if game_level1 < 5:
        new_enemy = enemies1[0]

    print(new_enemy)

create_enemy()



# Global scopes
enemies_g = "Skeleton"  # This is a global variable
def increase_enemies():
    enemies_g = "Zombie"  # This is a different variable due to local scope shadowing global
    print(f"Enemies inside function: {enemies_g}")

increase_enemies()
print(f"Enemies outside function: {enemies_g}")




# Usage of constants and "global" keyword best practice
# For constants, define them in uppercase:

PI = 3.14159
GOOGLE_URL = "https://www.google.com"
API_KEY = "***API_KEY***"

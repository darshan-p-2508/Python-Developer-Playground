"""
Higher or Lower Game:  
A simple Python game where the player guesses which celebrity or personality 
has more followers on social media.  
"""

import random
from game_data import data

def format_data(account):
    """
    Takes an account dictionary and formats it into
    a readable string with the person's name, description, and country.

    Args:
        account (dict): A dictionary containing account information.

    Returns:
        str: Formatted string with name, description, and country.
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """
    Compares the follower count of two accounts and checks
    if the user's guess is correct.

    Args:
        user_guess (str): The guessed option, 'a' or 'b'.
        a_followers (int): Follower count of Account A.
        b_followers (int): Follower count of Account B.

    Returns:
        bool: True if the user's guess is correct, False otherwise.
    """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
print("******* HIGHER or LOWER *******")
score = 0
game_should_continue = True

# Initialize with a random account
account_b = random.choice(data)

while game_should_continue:
    # Move account B to account A, and select a new account B
    account_a = account_b
    account_b = random.choice(data)
    if account_a ==  account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print("versus")
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # clear the screen by printing the empty lines to push the page upwards
    print("\n" * 25)
    print("******* HIGHER or LOWER *******")
    # print logo for every comparison
    
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score is: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score = {score}")
        game_should_continue = False


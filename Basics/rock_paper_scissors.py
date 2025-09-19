import random

user_choice = int(input("What do you choose?\n1.Rock\t2.Paper\t3.Scissors\n"))
if user_choice > 3:
    print("Wrong input. Choose from 1/2/3")
    exit(0)
    
choose_from = ["Rock", "Paper", "Scissors"]
computer_chooses = random.choice(choose_from)
user_chose = choose_from[user_choice - 1]

if computer_chooses == user_chose:
    print(f"You both chose {user_chose}. It's a draw")
if user_chose == "Rock":
    if computer_chooses == "Paper":
        print(f"{computer_chooses} beats {user_chose}. Computer Wins.")
    elif computer_chooses == "Scissors":
        print(f"{user_chose} beats {computer_chooses}. You Won.")
elif user_chose == "Paper":
    if computer_chooses == "Rock":
        print(f"{user_chose} beats {computer_chooses}. You Win.")
    elif computer_chooses == "Scissors":
        print(f"{computer_chooses} beats {user_chose}. Computer Wins.")
elif user_chose == "Scissors":
    if computer_chooses == "Paper":
        print(f"{user_chose} beats {computer_chooses}. You Win.")
    elif computer_chooses == "Rock":
        print(f"{computer_chooses} beats {user_chose}. Computer Wins.")

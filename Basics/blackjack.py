import random

def deal_cards():
    """ Returns a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Take a list of cards and returns the score calculated. """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(p_score, c_score):
    if(p_score == c_score):
        return "Draw"
    elif c_score == 0:
        return "You Lose, Opponent has a Blackjack."
    elif p_score == 0:
        return "You Win with a Blackjack."
    elif p_score > 21:
        return "You went over. You Lose."
    elif c_score > 21:
        return "Opponent went over. You Win."
    elif p_score > c_score:
        return "You Win."
    else:
        return "You Lose."

def play_game():
    player_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'Yes' to get another card, or 'No' to pass: ").lower()
            if user_should_deal == "yes":
                player_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while (input("Do you want to play a game of BlackJack? Type 'Yes' or 'No': ")).lower() == "yes":
    print("*" * 25)
    play_game()

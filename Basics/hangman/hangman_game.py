import random
from hangman_words import word_list
from hangman_arts import stats, logo

lives = 6
print(logo)

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
word_is = ""
for i in range(word_len):
    word_is += "_"
print("Word to guess: " + word_is)

game_status = False
correct_letters = []

while not game_status:
    print(f"{lives} / 6 lives left")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_status = True
            print(f"You lose!!! The correct word is: {chosen_word}")

    if "_" not in display:
        game_status = True
        print("You Win!!!")

    
    print(stats[lives])
        

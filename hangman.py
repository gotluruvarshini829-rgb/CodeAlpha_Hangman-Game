import random

# Step 1: List of words
words = ["apple", "tiger", "chair", "pizza", "robot"]

# Step 2: Choose a random word
secret_word = random.choice(words)

# Step 3: Variables
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")

# Step 4: Game loop
while wrong_guesses < max_guesses:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("Congratulations! You won!")
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check correct or wrong
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

    # Remaining attempts
    print("Remaining attempts:", max_guesses - wrong_guesses)

# Lose condition
if wrong_guesses == max_guesses:
    print("\nYou lost!")
    print("The word was:", secret_word)
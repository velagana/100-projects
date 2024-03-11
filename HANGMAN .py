#Hangman game
import random

def choose_word():
    # List of words for the game
    words = ["apple", "banana", "orange", "grape", "strawberry", "melon", "pineapple", "peach"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Guessed letters:", guessed_letters)
        print("Word:", display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Oops! That letter is not in the word.")
            guessed_letters.append(guess)
            attempts -= 1

    if attempts == 0:
        print("You're out of attempts! The word was:", word)

if __name__ == "__main__":
    hangman()

#This is a game for the user to guess the letters of a word 
#User only has 7 lives
#This code is written by znl_arad

import random
from words import words
import string


lives_visual_dict = {
    6: """
            ___________
           | /        | 
           |/        ( )
           |          |
           |         / \\
           |
       """,

    5: """
            ___________
           | /        | 
           |/        ( )
           |          |
           |          
           |
        """,
    4: """
            ___________
           | /        | 
           |/        ( )
           |          
           |          
           |
        """,
    3: """
            ___________
           | /        | 
           |/        
           |          
           |          
           |
        """,
    2: """
            ___________
           | /        
           |/        
           |          
           |          
           |
        """,
    1: """
           |
           |
           |
           |
           |
        """,
    0: "",
}

def get_words(words):
    word = random.choice(words)#randomly choosing a word from all random generated words list
    while len(word) > 5 or " " in word or "-" in word:#not allowing to generate a word more than 5 letters
        word = random.choice(words)
    return word

def display_word(word, guessed_letters):
    # Displaying the word with guessed letters and underscores for unguessed letters
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter #shows the correct guessed letter in the word by user
        else:
            display += '_'
    return display

def hangman():
    # Geting a random word from the list
    word_to_guess = get_words(words)
    
    # Initialize variables
    guessed_letters = set()
    incorrect_guesses = 0
    
    while incorrect_guesses < 7:
        # Display the current state of the word and hangman
        print(display_word(word_to_guess, guessed_letters))
        print(lives_visual_dict[incorrect_guesses]) #using the coresponding shape from dictionary according to user's left lives
        
        # Ask the user for a guess
        guess = input("Guess a letter: ").lower()
        
        # Check if the guess is a valid single letter
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        # Add the guessed letter 
        guessed_letters.add(guess)
        
        # Check if the guess is incorrect
        if guess not in word_to_guess:
            incorrect_guesses += 1
            print("Incorrect guess! Lives left:", 7 - incorrect_guesses)
        
        # Check if the player has guessed all letters and won
        if set(word_to_guess).issubset(guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break #ending the loop while
    
    # If the player has used all 7 lives, code shows the failed text and the correct generatedd word by random function
    if incorrect_guesses == 7:
        print("Sorry, you ran out of lives. The correct word was:", word_to_guess)

if __name__ == "__main__":
    # Run the hangman game
    hangman()
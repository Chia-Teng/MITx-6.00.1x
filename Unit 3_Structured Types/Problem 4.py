#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:35:25 2021

@author: teng
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    mistakesMade = 0
    lettersGuessed = []
    
    while True:  # I want it loop until the game ends

        # This block indicates how game ends (win or lose)
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("-----------\n"
                  "Congratulations, you won!")
            break  
        elif mistakesMade == 8:
            print("-----------\n"
                  "Sorry, you ran out of guesses. The word was else.")
            break

        # if the game doesn't end, continue guessing
        else:

            # tell the player guesses left and available letters
            print("-----------\n"
                  "You have " + str(8 - mistakesMade) + " guesses left.\n"
                  "Available letters: " + getAvailableLetters(lettersGuessed))

            # let the player enter a letter and transfer it to a lower case
            enter = input("Please guess a letter: ").lower()
            
            # prevent users from entering already guessed letters
            if enter in set(lettersGuessed):
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))

            # respond to newly guessed letters
            else:

                lettersGuessed.append(enter)

                if enter in set(secretWord):
                    print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                else:
                    print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                    mistakesMade += 1
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    return set(secretWord) - set(lettersGuessed) == set()

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    return "".join(l if l in lettersGuessed
                     else "_"
                   for l in secretWord)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
    return "".join(l for l in "abcdefghijklmnopqrstuvwxyz"
                   if l not in lettersGuessed)

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
    # FILL IN YOUR CODE HERE...

    # opening. tell the player the length of secretWord
    print("Welcome to the game Hangman!\nI am thinking of a word that is "
          + str(len(secretWord)), "letters long.")
    
    # initial values: they play haven't made a guess or made any mistake
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

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

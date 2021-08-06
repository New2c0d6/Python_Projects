import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open("C:\\Users\\NIMMY\\programmes\\python\\Hangman game\\words.txt", 'r')
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

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    return all([False for a in secretWord if a not in lettersGuessed])



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    return "".join([a if a in lettersGuessed else "_ " for a in secretWord])



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    return "".join([a for a in 'abcdefghijklmnopqrstuvwxyz' if a not in lettersGuessed])
    

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

    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    attempts = 8
    lettersGuessed = []
    while(attempts != 0):
        print("-----------")
        print("You have " + str(attempts) + " guesses left.")
        print("Available letters: ", getAvailableLetters(lettersGuessed) )
        guess = input("Please guess a letter: ")
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed) )
            continue
        else:
            lettersGuessed.append(guess.lower())
        if guess.lower() in secretWord:
            print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
            attempts -= 1
        if isWordGuessed(secretWord, lettersGuessed):
            print("-----------")
            print("Congratulations, you won!")
            return None
    print("-----------")
    print("Sorry, you ran out of guesses. The word was " + secretWord)
    return None


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

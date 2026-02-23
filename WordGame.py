#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for ch in word:
            if letter==ch:
                return True
    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    correctLetter=word[spot]
    if letter==correctLetter:
        return True
    else:
        return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback=""

    for spot in range(5):
        myLetter=myGuess[spot]
        if inSpot(myLetter, word, spot)==True:
            feedback=feedback+myLetter.upper()
        elif inWord(myLetter,word)==True:
            feedback=feedback+myLetter.lower()
        else:
            feedback=feedback+"*"
    return feedback

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)
    print("Here are some clues:")
    print("Uppercase letters indicate correct letters and placement,")
    print("Lowercase letters indicate correct letters but in the wrong spot,")
    print("'*' indicates a letter that is not in the word.")
    print("Good luck!")
    #User should get 6 guesses to guess
    #Ask user for their guess
    guessNumber=1
    while guessNumber<=6:
        validWord=False
        while validWord==False:
            guess=input("Time to enter your guess here!:")
            guess=guess.lower()
            if guess not in wordList:
                print("Word not in list.")
                validWord=False
            else:
                validWord=True
        feedback=rateGuess(guess,todayWord)
        print(feedback)
        if feedback==todayWord.upper():
            print("You got it in", guessNumber, "tries!!")
            break
        guessNumber=guessNumber+1
    print("The word was",todayWord)
    print("Thank you, come again!")





if __name__ == '__main__':
  main()

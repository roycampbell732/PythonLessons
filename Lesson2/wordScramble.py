# Introduction to Programming with Python
# Lesson 2 - Word Scramble Game
#
# Roy Campbell
#
# Modified from Lesson 1 - Guess the Number
# Required files: wordlist.txt

import random

keepPlaying = True

with open('wordlist.txt', 'r') as wl:
    wordList = wl.read().split()

shortest = 3
longest = len(max(wordList, key=len))

while keepPlaying:
    print("")
    wordLength = 0
    while wordLength < shortest or wordLength > longest:
        wordLength = input(f"How many letters should be in your word? (number between {shortest} and {longest}) ")
        try:
            wordLength = int(wordLength)
            wordLengthIsInt = True
        except ValueError:
            wordLengthIsInt = False
            wordLength = 0
        if wordLength < shortest or wordLength > longest:
            print(f"Please enter a number between {shortest} and {longest}")
            print("")

    wordPickList = [word for word in wordList if len(word) == wordLength]
    secretWord = random.choice(wordPickList)
    scrambled = random.sample(secretWord, len(secretWord))
    scrambled = ''.join(scrambled)
    guess = ''
    tryAgain = "y"
    while guess == '':
        print(f"Your scrambled word is {scrambled}")
        guess = input(f"Enter your answer: ")

    print("")
    if guess.lower() == secretWord.lower():
        print(f"Correct! The scrambled word {scrambled} is {guess}")
    else:
        print(f"Incorrect! The scrambled word {scrambled} is {secretWord}")
    print("")

    tryAgain = input("Keep Playing? (Y/n) ")
    if not tryAgain:  # test for enter without character and set to "y" as default
        tryAgain = "y"
    if tryAgain.lower() != "y":
        keepPlaying = False

print("")
print("Thanks for Playing!")
print("-------------------")
exit()



# additional challenges:
# 1. improve the script such that it tests the guess to make sure it's the correct length
# 2. improve the script such that it tests the guess to verify it contains the correct letters
# 3. if you really feel adventurous, on incorrect guesses,
#       let the user know which letters are in the correct place
#       and then ask them for another guess.

# the first improvement is:
'''
        if len(guess) != wordLength:
            print(f"Your guess needs to be {wordLength} letters long.")
            guess = ''
'''
# copy the code between the 3 quotes and paste it where it belongs in the script

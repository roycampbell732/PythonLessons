

import random

keepPlaying = True

with open('wordlist', 'r') as wl:
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

    wordListLength = [word for word in wordList if len(word) == wordLength]
    secretWord = random.choice(wordListLength)
    jumble = random.sample(secretWord, len(secretWord))
    jumble = ''.join(jumble)
    guess = ''
    tryAgain = "y"
    while guess != secretWord and tryAgain == "y":
        print(f"The jumble word is: {jumble}")
        print("")
        guess = input(f"Type your guess: ")
        print("")
        condition = True
        if len(guess) != len(secretWord):
            print(f"Your guess doesn't have {len(secretWord)} letters.")
            condition = False

        if condition:
            charNum = 0
            while charNum < len(secretWord):
                if guess[charNum] not in secretWord:
                    print(f"Oops, a typo occurred. The letter '{guess[charNum]}' is not in the jumble. Please try "
                          f"again.")
                    condition = False
                elif guess[charNum] != secretWord[charNum]:
                    print(f"Oops, a typo occurred.  The letter'{guess[charNum]}' is in the wrong place. Please try "
                          f"again.")
                    condition = False
                charNum += 1
        if guess.lower() != secretWord.lower() and condition:
            tryAgain = input(f"Incorrect!  Would you like to try again? (Y/n) ")
            if not tryAgain:  # test for enter without character and set to "y" as default
                tryAgain = "y"
            if tryAgain.lower() != "y":
                tryAgain = "n"

    if guess.lower() == secretWord.lower():
        print(f"Correct! The scrambled word {jumble} is {guess}")
    else:
        print(f"The scrambled word {jumble} is {secretWord}")
    print("")
    keepPlaying = input("Keep Playing? (Y/n) ")
    if not keepPlaying:  # test for enter without character and set to "y" as default
        keepPlaying = "y"
    if keepPlaying.lower() != "y":
        print("Thanks for Playing")
        print("--------------------")
        exit()


# additional challenges:
# 1. improve the script such that it tests the guess to make sure it's the correct length
# 2. improve the script such that it tests the guess to verify it contains the correct letters
# 3. if you really feel adventurous, on incorrect guesses,
#       let the user know which letters are in the correct place.


# Introduction to Python Programming
# Roy Campbell
#
# Guess the Number Game
# Inspired originally from a Matt Macarty YouTube video at: https://youtu.be/7CTONNO6YMc

import random

print("Welcome to the number guessing game")
print("")
print("Try to guess the number I'm thinking of.")
print("It's between 1 and 100")
print("You will have up to 6 tries to guess the number.")
print("")

keepTrying = True

while keepTrying:
    secretNumber = random.randint(1, 100)
    guess = 0
    tries = 0
    while guess != secretNumber and tries < 6:
        guess = input("What is your guess (between 1 & 100)? ")
        guess = int(guess)

        if guess > secretNumber:
            print("Your guess is too high.")
        elif guess < secretNumber:
            print("Your guess is too low.")
        tries += 1

    if guess == secretNumber:
        print("Well Done!!  You guessed my number.")
    else:
        print("Sorry. Better luck next time.")
        print("The secret number was", secretNumber)

    tryAgain = input("Would you like to try again? (y/n) ")
    if tryAgain.lower() != "y":
        keepTrying = False

print("")
exit(print("Thanks for playing!"))
### Additional Challenges



1. improve the script such that it tests the guess to make sure it's the correct length
2. improve the script such that it tests the guess to verify it contains the correct letters
3. if you really feel adventurous, on incorrect guesses,
       let the user know which letters are in the correct place
       and then ask them for another guess.

The first improvement is:
```
        if len(guess) != wordLength:
            print(f"Your guess needs to be {wordLength} letters long.")
            guess = ''
```
Copy the code and paste it where it belongs in the script

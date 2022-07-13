## The Challenge

from [Python Programming Challenge – First to Five – Real Python](https://realpython.com/python-programming-contest-first-to-five/)



1. There are two players.
2. Each player writes a number, hidden from the other player. It can be any integer 1 or greater.
3. The players reveal their numbers.
4. Whoever chose the lower number gets 1 point, unless the lower number is lower by only 1, then the player with the higher number gets 2 points.
5. If they both chose the same number, neither player gets a point.
6. This repeats, and the game ends when one player has 5 points.

The challenge is to write a script to play this game. Knowing the rules and all your opponent’s previous numbers, can you program a strategy? (And, no - `return random.randint(1, 3)` is not a strategy.) You should really try playing this first with your friends - you’ll see there’s a deep human element to predicting your opponent’s choice.

Is it possible to program a strong strategy?

Make the game so the player plays against the computer and try to make it so the computer.

Want to make the strategy a bit more interesting? Add an additional constraint to the challenge so that players can only use each number once.

The 2 player version is as follows:

```python
import pandas as pd
import numpy as np

player1 = 0
player2 = 0
score1 = 0
score2 = 0

while (score1 < 5) and (score2 < 5):
  player1 = input("Enter player1's number: ")
  player2 = input("Enter player2's number: ")
  player1 = int(player1)
  player2 = int(player2)
  print("Player1's number is ", player1)
  print("Player2's number is ", player2)
  if player1 < (player2 - 1):
    score1 = score1 + 1
  if player1 == (player2 - 1):
    score2 = score2 + 2
  if player2 < (player1 - 1):
    score2 = score2 + 1
  if player2 == (player1 - 1):
    score1 = score1 + 2
  print("Score1 is ", score1)
  print("Score2 is ", score2)
print("Stop game")
if score1 > score2:
  print("Contragulations player1, you are the winner!")
else:
  print("Congratulations player2, you are the winner!")
```

Good Luck

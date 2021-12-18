```python

# 4. start the game
response = ""
while True:
  response = input("\nWhich direction would you like to move to? [left], [right], [up], [down]: ")
  if response == "left" or response == "l":
    print("move to left")  # we need to decide what to do if the user want to move to left
  elif response == "right" or response == "r":
    print("move to right")  # we need to decide what to do if the user want to move to rigth
  elif response == "up" or response == "u":
    print("move up")  # we need to decide what to do if the user want to move up
  elif response == "down" or response == "d":
    print("move down")  # we need to decide what to do if the user want to move down
  elif response == "quit" or response == "exit":
    print("\nThanks for playing this game, bye-bye!")
    break;
  else:
    print("Invalid move, try again.")

```

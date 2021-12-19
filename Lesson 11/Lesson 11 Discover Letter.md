```python

def discover_letter():
  print(smart_move_msg)
  # below print statement is for debugging purpose, disable it when playing the game
  # print("current row: " + str(current_row), "current column: " + str(current_col))  
  if forest[current_row][current_col] != "":
    letter = forest[current_row][current_col]
    print("You have discovered a letter: " + letter)
    letter_list.append(letter)
    forest[current_row][current_col] = ""   # set this cell to empty as the letter is discovered  
  if len(letter_list) == word_length:
    print("\nCongratulation! You have discovered all the letters.")
    print(letter_list)
    print("\nYour final task is to guess the secret word.")
    guess = input("What is the secret word in your mind? ")
    if(guess.upper() == secret_word.upper()):
      print_winner_message()
      return "WIN"
    else:
      print("Wrong guess!")  
      print_gameover_message()
      return "LOSE"
  else:
    return "CONTINUE"
    

def print_winner_message():
  print("\nYou did it! Your mission is completed!")
  print("* * * * * * * * * * * * * * * * * * * * * * *")
  print("*            You are the WINNER!            *")
  print("* * * * * * * * * * * * * * * * * * * * * * *")


def print_gameover_message():
  print("\nYou lost the game!")
  print("* * * * * * * * * * * * * * * * * * * * * * *")
  print("*                GAME OVER!                 *")
  print("* * * * * * * * * * * * * * * * * * * * * * *")

```

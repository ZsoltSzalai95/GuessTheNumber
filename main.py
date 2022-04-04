#Number Guessing Game Objectives:

#1 Have the modules ready
import random
from random import randint

#2 Set up the level variables with the global scope
TURNS_EASY=10
TURNS_HARD=5

#3 Set up a function that checks wheather the user guess is correct. 
def check_the_answer(guess,answer,turns):
  """This function checks the user guess against the actual answer, and it returns the number of attempts left."""
  if guess>answer:
    print("Too high!")
    return turns-1
  elif guess<answer:
    print("Too low!")
    return turns-1
  else:
    print(f"Congratulations. You have guessed my number, namely {answer}!")

#4 Set up function to return the global variables based on difficulty level
def difficulty_level():
  levels=input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
  if levels=="easy":
    return TURNS_EASY
  elif levels=="hard":
    return TURNS_HARD

#5 Set up final function that will run the game and keep count of the remaining attempts left.
def game():
  from art import logo
  print(logo)
  answer=random.randint(1,100)

  print(f"Welcome to the Number Guessing Game!\nI'm thinking of"
        f"a number between 1 and 100.\nPssst, the correct answer is {answer}")
  turns=difficulty_level()

  
  #6Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess!=answer:
    print(f"You have {turns} attempts left.")
    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_the_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, game over. ☠️")
      return
    elif guess != answer:
      print("Guess again.")

    

game()



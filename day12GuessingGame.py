from art import numlogo
import random

easyLevel = 10
hardLevel = 5

def checkAnswer(guess, answer, turn):
  if guess > answer:
    print("Too high")
    return turn - 1
  elif answer > guess:
    print("Too low")
    return turn - 1
  else:
    print(f"That's right! the answer is {answer}")

def setDifficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return easyLevel
  else:
    return hardLevel

def game():
  print(numlogo)
  print('Welcome to the number guessing game!')
  print('I\'m thinking of a number between 1 and 100.')
  answer = random.randint(1, 100)

  turn = setDifficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turn} turns left to guess the answer.")
    guess = int(input("Make a guess: "))

    turn = checkAnswer(guess, answer, turn)
    if turn == 0:
      print(f"You've run out of guesses. You lose. ")
      return
    elif guess != answer:
      print('Guess again')


game()

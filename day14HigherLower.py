# players must guess which person has the most instagram followers
# if they guess right they move on to the next person and their score is counted (person b from the previous round becomes person a in the next round), if they guess wrong the game ends and their score is printed
# the game continues until they guess wrong

# todo: import art and game data
from art import hllogo, vs
from game_data import data
import random

# todo: welcome player to game and brief intro
print(hllogo)
print("Welcome to the higher lower game! Guess which instagram acoount has more followers!")

score = 0
gameContinues = True
accountB = random.choice(data)

while gameContinues:
  def format_data(account):
    """format the account data"""
    accountName = account["name"]
    accountDesc = account["description"]
    accountCountry =account["country"]
    return(f'{accountName}, a {accountDesc} from {accountCountry}')

  def check_answer(choice, aFollowers, bFollowers):
    """Use if statement to check if answer is correct"""
    if aFollowers > bFollowers:
      return choice == 'a'
    else:
      return choice == 'b'


  #display random a and b info and ask user whether a or b has more followers
  #generate random account from the game data
  accountA = accountB
  accountB = random.choice(data)
  while accountA == accountB:
    accountB = random.choice(data)

  print(f"Compare A: {format_data(accountA)}")
  print(vs)
  print(f"Against B: {format_data(accountB)}")

  choice = input("Who has more followers? Type 'A' or 'B': ").lower()

  aFollowers = accountA["follower_count"]
  bFollowers = accountB["follower_count"]
  #check whether the user has the right answer
  isCorrect = check_answer(choice, aFollowers, bFollowers)

  #give the user feedback
  if isCorrect:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    gameContinues = False
    print(f"Sorry, that's wrong. Final score: {score}")

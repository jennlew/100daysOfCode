# players must guess which person has the most instagram followers
# if they guess right they move on to the next person and their score is counted (person b from the previous round becomes person a in the next round), if they guess wrong the game ends and their score is printed
# the game continues until they guess wrong

# todo: import art and game data
from art import hllogo, vs
from game_data import data
import random

# todo: welcome player to game and brief intro
print(logo)
print("Welcome to the higher lower game! Guess which instagram acoount has more followers!")

def format_data(account):
  """format the account data"""
  accountName = account["name"]
  accountDesc = account["description"]
  accountCountry =account["country"]
  return(f'{accountName}, a {accountDesc} from {accountCountry}')

def check_answer(choice, aFollowerCount, bFollowerCount):
  """Use if statement to check if answer is correct"""


# todo: display random a and b info and ask user whether a or b has more followers
#generate random account from the game data
accountA = random.choice(data)
accountB = random.choice(data)
if accountA == accountB:
  accountB = random.choice(data)

print(f"Compare A: {format_data(accountA)}")
print(vs)
print(f"Against B: {format_data(accountB)}")

choice = input("Who has more followers? Type 'A' or 'B': ").lower()

aFollowerCount = accountA["follower_count"]
bFollowerCount = accountB["follower_count"]
# todo: check whether the user has the right answer
# make sure that you get the index of the dictionary item that is the number of followers
#
  #if A[i] > B[i] and choice == "A"
    #keep A to move on to the next round
    #choose new opponent
    #repeat
  #elif B[i] > A[i] and choice == "B"
    #turn B into A for next round
    #choose new opponent
    #repeat
  #else
    #end game
# todo: if the user has the right answer add a point to their total
# todo: if the user has the right answer make person b person a for the next round
# todo: if the user has the wrong answer end the game and show them their total score

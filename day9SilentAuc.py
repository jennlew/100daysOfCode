from replit import clear
from artday9 import logo
#HINT: You can call clear() to clear the output in the console.

bids = {}

print(logo)
print("Welcome to the Secret Auction Program")
bidding_finished = False

def find_highest_bid(bids):
  highest_bid = 0
  winner = ''
  for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f'The winner is {winner} with a bid of ${highest_bid}')

while not bidding_finished:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids[name] = bid
  continuing = input("Are there any other bidders? Type 'yes' or 'no': ")
  if continuing == 'no':
    bidding_finished = True
    find_highest_bid(bids)
  elif continuing == 'yes':
    clear()

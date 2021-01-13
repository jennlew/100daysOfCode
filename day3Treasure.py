print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
leftRight = input('You are faced with two choices, left or right. Which one do you choose? ')

if leftRight.lower() == 'left':
  print("Phew! You just missed that hole! Now you can move on to the next step. ")

  swimWait = input('The tide is high! Do you want to swim or wait?')

  if swimWait.lower() == 'wait':
    print("The tide is low now! Here's your chance to move on to the next step! ")

    door = input('There are three doors to choose from! Which one will you go for red, \n blue or yellow?? ')

    if door.lower() == 'yellow':
      print("You made it, you found the treasure! You win, congratulations!!")
    elif door.lower() == 'blue':
      print("You were eaten by beasts :( \n Game over.")
    elif door.lower() == 'red':
      print("You were burned by fire :( \n Game over.")
    else:
      print("That was not an option. GAME OVER.")
  elif swimWait.lower() == 'swim':
    print("You were attacked by a trout :( \n Game over.")
  else:
    print('That was not an option. Game over.')
elif leftRight.lower() == 'right':
  print('Damn! You fell into a hole. Game over.')
else:
  print('That was not an option. Game over.')

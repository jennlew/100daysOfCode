import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves = ['rock', 'paper', 'scissors']
computer = random.randint(0,2)

player = input('Let\'s play rock, paper, scissors! Type 0 for rock, 1 for paper or 2 for scissors: ')
playerChoice = moves[int(player)]
computerChoice = moves[computer]

if playerChoice == 'rock' and computerChoice == 'scissors':
  print(f'You chose rock! \n{rock}\n Computer chose scissors!\n {scissors}\n You win!')
elif playerChoice == 'paper' and computerChoice == 'rock':
  print(f'You chose paper! \n{paper}\n Computer chose rock!\n {rock}\n You win!')
elif playerChoice == 'scissors' and computerChoice == 'paper':
  print(f'You chose scissors! \n{scissors}\n Computer chose paper!\n {paper}\n You win!')
elif playerChoice == 'rock' and computerChoice == 'paper':
  print(f'You chose rock! \n{rock}\n Computer chose paper!\n {paper}\n You lose!')
elif playerChoice == 'paper' and computerChoice == 'rock':
  print(f'You chose paper! \n{paper}\n Computer chose scissors!\n {scissors}\n You lose!')
elif playerChoice == 'scissors' and computerChoice == 'rock':
  print(f'You chose scissors! \n{scissors}\n Computer chose rock!\n {rock}\n You lose!')
elif playerChoice == computerChoice:
  print('You and computer chose the same thing, it\'s a draw!')
else:
  print('that was not a valid move')

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowerName1 = name1.lower()
lowerName2 = name2.lower()

trueCount = 0
loveCount = 0
if lowerName1.count('t') > 0:
  trueCount = trueCount + lowerName1.count('t')
if lowerName1.count('r') > 0:
  trueCount = trueCount + lowerName1.count('r')
if lowerName1.count('u') > 0:
  trueCount = trueCount + lowerName1.count('u')
if lowerName1.count('e') > 0:
  trueCount = trueCount + lowerName1.count('e')
if lowerName2.count('t') > 0:
  trueCount = trueCount + lowerName2.count('t')
if lowerName2.count('r') > 0:
  trueCount = trueCount + lowerName2.count('r')
if lowerName2.count('u') > 0:
  trueCount = trueCount + lowerName2.count('u')
if lowerName2.count('e') > 0:
  trueCount = trueCount + lowerName2.count('e')
if lowerName1.count('l') > 0:
  loveCount = loveCount + lowerName1.count('l')
if lowerName1.count('o') > 0:
  loveCount = loveCount + lowerName1.count('o')
if lowerName1.count('v') > 0:
  loveCount = loveCount + lowerName1.count('v')
if lowerName1.count('e') > 0:
  loveCount = loveCount + lowerName1.count('e')
if lowerName2.count('l') > 0:
  loveCount = loveCount + lowerName2.count('l')
if lowerName2.count('o') > 0:
  loveCount = loveCount + lowerName2.count('o')
if lowerName2.count('v') > 0:
  loveCount = loveCount + lowerName2.count('v')
if lowerName2.count('e') > 0:
  loveCount = loveCount + lowerName2.count('e')

loveScore = int(str(trueCount) + str(loveCount))

if loveScore < 10 or loveScore > 90:
  print(f'Your score is {loveScore}, you go together like coke and mentos.')
elif loveScore >= 40 and loveScore <= 50:
  print(f'Your score is {loveScore}, you are alright together.')
else:
  print(f'Your score is {loveScore}.')

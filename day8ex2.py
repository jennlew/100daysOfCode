#Write your code below this line 👇

def prime_checker(number):
  prime_num = True
  for num in range(2, number):
    if number % num == 0:
      prime_num = False

  if prime_num == True:
    print('It\'s a prime number')
  else:
    print('It\'s not a prime number')

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

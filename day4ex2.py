# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
length = len(names)
whosPaying = random.randint(1, length - 1)
# print(names[whosPaying])
print(f'{names[whosPaying]} is going to buy the meal today!')

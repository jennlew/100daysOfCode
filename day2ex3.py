# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
goalAge = 90
goalAgeMonths = 90 * 12
goalAgeWeeks = 90 * 52
goalAgeDays = 90 * 365

ageMonths = int(age) * 12
ageWeeks = int(age) * 52
ageDays = int(age) * 365

monthsLeft = goalAgeMonths - ageMonths
weeksLeft = goalAgeWeeks - ageWeeks
daysLeft = goalAgeDays - ageDays

print(f'You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left. \n')

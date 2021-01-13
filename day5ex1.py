# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#create variables to store looped values
total_height = 0
count = 0

# loop to add all the heights together and count how many there are
for height in student_heights:
  total_height += height
  count += 1

#print values
print(total_height)
print(count)

#math to work out the average then print average
average_height = round(total_height / count)
print("The average height of the students is: ", average_height)

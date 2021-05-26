import random

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)
result = [num for num in numbers if num % 2 == 0]
print(result)

with open('file1.txt') as file1:
    file1_nums = file1.readlines()

with open('file2.txt') as file2:
    file2_nums = file2.readlines()

result2 = [int(n) for n in file1_nums if n in file2_nums]
print(file1_nums)
print(result2)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_result = {word: len(word) for word in sentence.split()}
print(sentence_result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)
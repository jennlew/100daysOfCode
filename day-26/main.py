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

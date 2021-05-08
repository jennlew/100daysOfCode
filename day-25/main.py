import csv
import pandas as pd

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pd.read_csv("weather_data.csv")
type(data)

data_dict = data.to_dict()
temp_list = data["temp"].to_list()

avg = 0
for temp in temp_list:
    avg += temp

avg = avg / len(temp_list)
print(avg)

print(data["temp"].max())
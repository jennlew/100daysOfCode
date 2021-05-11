import csv
import pandas as pd

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pd.read_csv("weather_data.csv")
# type(data)
#
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
#
# avg = 0
# for temp in temp_list:
#     avg += temp
#
# avg = avg / len(temp_list)
# print(avg)
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = 0
cinnamon = 0
black = 0
for color in df["Primary Fur Color"]:
    if color == "Gray":
        grey += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1

color_count = pd.DataFrame({"Fur colour": ["grey", "red", "black"],
                            "Count": [grey, cinnamon, black]})

color_count.to_csv("squirrel_count.csv")

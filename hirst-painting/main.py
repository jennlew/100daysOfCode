# import colorgram
#
# colours = colorgram.extract('image.jpg', 20)
# rgb_colours = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)
import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.speed(10)
tim.penup()
tim.hideturtle()
colour_list = [(235, 234, 231), (236, 228, 232), (226, 238, 231), (223, 231, 239), (237, 36, 111), (150, 24, 66), (215, 167, 53), (8, 146, 90), (240, 72, 34), (186, 161, 41), (27, 127, 194), (47, 190, 233), (245, 219, 49), (181, 38, 100), (81, 24, 87), (126, 192, 92), (252, 225, 0), (22, 170, 125), (219, 57, 21), (213, 133, 169)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()

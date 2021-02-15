from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.width(5)
# for i in range(15):
#     timmy.down()
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)

colours = ["aquamarine", "deep pink", "pale turquoise", "powder blue", "light pink", "thistle", "plum", "misty rose"]


def draw_shape(sides):
    angle = 360 / sides
    for i in range(sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_sides in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_sides)

screen = Screen()
screen.exitonclick()

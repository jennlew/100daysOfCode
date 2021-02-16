import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


timmy.shape("turtle")
timmy.width(3)
timmy.speed(0)


def draw_circles(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_circles(5)

screen = t.Screen()
screen.exitonclick()


# for i in range(15):
#     timmy.down()
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)

# def draw_shape(sides):
#     angle = 360 / sides
#     for i in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_sides in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_sides)

# colours = ["aquamarine", "deep pink", "pale turquoise", "powder blue", "light pink", "thistle", "plum", "misty rose"]
# directions = [0, 90, 180, 270]
#
# for i in range(200):
#     timmy.color(random_colour())
#     timmy.forward(40)
#     timmy.setheading(random.choice(directions))

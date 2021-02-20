from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(clockwise, 'd')
screen.onkey(counter_clockwise, 'a')
screen.onkey(clear, 'c')
screen.exitonclick()

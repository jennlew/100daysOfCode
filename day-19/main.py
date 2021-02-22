from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])

# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def counter_clockwise():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def clockwise():
#     tim.right(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards, 'w')
# screen.onkey(move_backwards, 's')
# screen.onkey(clockwise, 'd')
# screen.onkey(counter_clockwise, 'a')
# screen.onkey(clear, 'c')
screen.exitonclick()

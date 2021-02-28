from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    for turt_num in range(len(turtles) - 1, 0, -1):
        new_x = turtles[turt_num - 1].xcor()
        new_y = turtles[turt_num - 1].ycor()
        turtles[turt_num].goto(new_x, new_y)

    turtles[0].forward(20)


screen.exitonclick()

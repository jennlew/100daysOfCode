import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
answer_state = answer_state.title()

df = pd.read_csv("50_states.csv")
all_states = df["state"].tolist()
correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 states correct", prompt="What's another state's "
                                                                                              "name?").title()

    if answer_state in all_states:
        correct_answers.append(answer_state)
        turtle.hideturtle()
        turtle.penup()
        state_data = df[df.state == answer_state]
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(answer_state)





screen.exitonclick()
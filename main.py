import turtle
import pandas
import pandas as pd

data = pd.read_csv("50_states.csv")
states_name = data.state.to_list()
IMAGE = "blank_states_img.gif"
guess_state = []

screen = turtle.Screen()
screen.title("U.S State Guess!!")
screen.addshape(IMAGE)
turtle.shape(IMAGE)


while len(guess_state) < 50:
    answer = screen.textinput(title=f"{len(guess_state)}/50, Guess the state!!",
                              prompt="What's another state name?").title()
    if answer in states_name:
        guess_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer)

    if answer == "Exit":
        missing_state = []
        for state in states_name:
            if state not in guess_state:
                missing_state.append(state)

        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")

        break
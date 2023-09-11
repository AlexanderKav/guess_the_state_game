import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()
#def get_mouse_click_coor(x,y):
 #   print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()


import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
user_answers = []
tim.hideturtle()

score = 0
game_is_on = True
while game_is_on:

    if score == 50:
        game_is_on = False

    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in user_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False

    tim.home()
    count = -1
    for answer in data["state"]:
        count = count + 1

        if answer == answer_state:
            user_answers.append(answer)
            score = score + 1

            x_value = data.x[count]
            y_value = data.y[count]
            x_value = x_value
            y_value = y_value
            tim.penup()
            tim.goto(x_value, y_value)
            tim.write(arg=f"{answer_state}", font=('Arial', 8, 'normal'))


screen.exitonclick()
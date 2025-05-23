import turtle
screen = turtle.Screen()
screen.title("U.S. state game")
image = "blank_states_img.gif"
# adds image as a shape of turtle
screen.addshape(image)
turtle.shape(image)

# getting coords manually
# function to get x and y coord
# def get_coord(x,y):
#     print(x,y)
#
# # We will get the coord on screen click
# turtle.onscreenclick(get_coord)
#
# # this will loop the screen. meaning the screen will be open even if the click event occurs
# turtle.mainloop()

# We don't need this since we already have the x and y coordinates in our 50 states.csv. We can read it and use the values


# print(answer_state)
import pandas
# reading the file
data = pandas.read_csv("50_states.csv")
# converting the data to list
states = data.state.to_list()
# creating a counter array
guessed_state = []

while len(guessed_state) < 50:
    # asking user input
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states guessed", prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        # checking how many states are remaining. If it has remaining states, we store them to a csv.
        missing_states = []
        for state in states:
            if state not in guessed_state:
                missing_states.append(state)
        # creating dataframe of the missing states array
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learn.csv")
        break

    # if the user types in a state's name
    if answer_state in states:
        # appending the correct answer in the guessed state array
        guessed_state.append(answer_state)
        # creating turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # taking out the row at which the answered state is present
        state_data = data[data.state == answer_state]
        # Locating it on the map and going to it's coordinates
        t.goto(state_data.x.item() , state_data.y.item())
        # writing the answer (state's name) on that position
        t.write(answer_state)


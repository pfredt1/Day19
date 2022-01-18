from turtle import Turtle, Screen
import random


# tim = Turtle(shape="turtle")

screen = Screen()
x_start = -240
y_start = -180
colors = ["red", "orange", "black", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
is_race_on = False


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet ", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=x_start, y=y_positions[turtle_index])
    turtles.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        rand_distance = random.randint(0, 30)
        t.forward(rand_distance)
        if t.xcor() >= 230:
            is_race_on = False
            if user_bet == t.pencolor():
                print("You Win")
            else:
                print("you loose")









# tim.goto(x_start,y_start)

screen.listen()

screen.exitonclick()

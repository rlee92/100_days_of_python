from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width=500, height=400)

is_race_on = False
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_coordinates = [-75, -50, -25, 0, 25, 50, 75]
all_turtles = []

for turtle_index in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=start_coordinates[turtle_index])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)





s.exitonclick()
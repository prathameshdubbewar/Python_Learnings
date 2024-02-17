import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 500)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="The turtle that will win the race? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_posi = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_posi[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win the bet on your {winning_color} turtle")
            else:
                print(f"you lose, the {winning_color} turtle won the race")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)
screen.exitonclick()

# def move_forward():
#     tim.forward(10)
# def move_bacwrd():
#     tim.backward(10)
# def turn_left():
#     # tim.left(90)
#     # or can also use
#     tim.setheading(tim.heading() + 90)
#     tim.forward(10)
# def turn_right():
#     tim.right(90)
#     # or can also use
#     # tim.setheading(tim.heading() - 90)
#     tim.forward(10)
# def clear_scrn():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="s", fun=move_bacwrd)
# screen.onkey(move_forward, "w")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_scrn, "c")


# using turtle module for graphics
from turtle import Turtle, Screen
import random
# Or can also be written as
import turtle as t

tim = t.Turtle()
timmy = Turtle()
tim.shape("turtle")

colors = ["DarkOrchid", "Coral", "GreenYellow"]
# taking colormode from turtle
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


directions = [0, 90, 180, 270]
tim.speed("fastest")
# fastest = 0,fast=10,normal=6,slow=3,slowest = 1

# for i in range(15):
#
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()


# Increasing sides shape
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        # angle = 360/num_sides
        tim.pensize(15)
        tim.forward(100)
        tim.right(angle)


# for i in range(3, 11):
#     tim.pensize(15)
#     tim.color(random.choice(colors))
#     draw_shape(i)


# random movement with random colors
# for i in range(200):
#     tim.forward(30)
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))

def spiral_graph(gap_size):

    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

spiral_graph(5)

screen = Screen()
screen.exitonclick()

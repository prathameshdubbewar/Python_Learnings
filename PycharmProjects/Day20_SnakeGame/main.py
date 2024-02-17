from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# seg1 = Turtle("square")
# seg1.color("white")
#
# seg2 = Turtle("square")
# seg2.color("white")
# seg2.goto(-20, 0)
#
# seg3 = Turtle("square")
# seg3.color("white")
# seg3.goto(-40, 0)

# Or can be written as

positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for i in positions:
    new_seg = Turtle("circle")
    new_seg.color("red")
    new_seg.penup()
    new_seg.goto(i)
    segments.append(new_seg)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(26)



screen.exitonclick()

# Day 18 - Turtle & GUI
import random
from turtle import Turtle, done, Screen
import colorgram
my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('black')
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.lt(90)
# for _ in range(10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(5)
#     my_turtle.pendown()

# done()
colors = ["cornflower blue", "cadet blue", "plum","violet", "pink", "aquamarine", "lawn green", "orange red"]
# for sides in range(3,11):
#     for i in range(sides):
#         my_turtle.color(random.choice(colors))
#         my_turtle.forward(100)
#         my_turtle.rt(360/sides)

# done()
# my_turtle.hideturtle()
# my_turtle.width(12)
# my_turtle.speed('fastest')
# directions = [0, 90, 180, 270]
# while True:
#     my_turtle.pencolor(random.random(), random.random(),random.random())
#     my_turtle.forward(24)
#     my_turtle.setheading(random.choice(directions))

# done() 

# no_of_circles = 100
# my_turtle.hideturtle()
# my_turtle.speed('fastest')
# for _ in range (no_of_circles):
#     my_turtle.pencolor(random.random(), random.random(),random.random())
#     my_turtle.circle(100)
#     my_turtle.left(360/no_of_circles)
# done()


my_screen = Screen()
my_screen.setup(1080, 720)
my_screen.colormode(255)
colors = [color.rgb for color in colorgram.extract('Day18_hirst_painting.jpg', 25)]
my_turtle.hideturtle()

init_x = -300
init_y = -280
my_turtle.speed('fastest')
pos_y = init_y
for y in range(10):
    pos_x = init_x
    my_turtle.pu()
    my_turtle.goto(pos_x, pos_y)
    for x in range(10):
        color = random.choice(colors)
        my_turtle.color(color)
        my_turtle.dot(20, color)
        my_turtle.forward(50)
    pos_y += 50
done()
# Day 19 More turtle, higher order functions, state managements, event listeners
from turtle import Screen, Turtle, done
import random
# screen = Screen()
# t = Turtle()

# screen.listen()
# # etche a sketch
# k_right = False
# k_left = False
# k_forward = False
# def go_right():
#     global k_right
#     global k_forward
#     # print("Im here")
#     k_right = True
#     # print(k_right)
#     t.rt(10)
#     if k_forward:
#         t.fd(5)

# def go_left():
#     global k_left
#     global k_forward
#     k_left = True
#     t.lt(10)
#     if k_forward:
#         t.fd(5)
# def stop_right():
#     global k_right
#     k_right = False
    
# def stop_left():
#     global k_left
#     k_left = False
    
# def fw():
#     global k_forward
#     global k_right
#     global k_left
#     k_forward = True
#     print(k_right)
#     # print(k_left)
#     if k_right:
#         t.rt(10)
#     elif k_left:
#         t.lt(10)
#     t.fd(10)
# def stop_fw():
#     global k_forward
#     k_forward = False
# screen.onkeypress(fw, key='w')
# screen.onkeypress(go_right, key='d')
# screen.onkeypress(go_left, key='a')
# screen.onkeyrelease(stop_right, key='d')
# screen.onkeyrelease(stop_left, key='a')
# screen.onkeyrelease(stop_fw, key='w')
# screen.onkeypress(lambda : t.fd(-5), key='s')
# screen.onkeypress(lambda : t.reset(), key='c')


# # screen.title("Welcome to the horse racer")
# # screen.textinput("Bid Window", "Horse Color: ")
# done()



screen = Screen()
turtle_number = 6
colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
dist_between_turtles = 60
turtle_init_xpos = -220
turtle_init_ypos = -1 * 2.5 * dist_between_turtles
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtles = []
tempTurtle = Turtle(shape="turtle")
tempTurtle.hideturtle()
win_boundary = 230
tempTurtle.pu()
tempTurtle.goto(230, turtle_init_ypos-20)
tempTurtle.pd()
tempTurtle.goto(230, -turtle_init_ypos+20)
tempTurtle.pu()
for i in range(turtle_number):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
   
for i in range(turtle_number):
    turtles[i].pu()
    turtles[i].goto(x = turtle_init_xpos, y = turtle_init_ypos)
    turtle_init_ypos += 60
win = ""
while win == "":
    for i in range(len(turtles)):
        t = turtles[i]
        t.forward(random.randint(3,7))
        if t.position()[0]>=220:
            win = colors[i]
            break

tempTurtle.pu()
tempTurtle.goto(0,0)
if user_bet.lower() == win.lower():
    tempTurtle.write(f"First place: {win.title()}", True, align="center")
    
    tempTurtle.goto(0,-20)
    tempTurtle.write("You Win!", True, align="center")
else:
    tempTurtle.write(f"First place: {win.title()}", True, align="center")
    
    tempTurtle.goto(0,-20)
    tempTurtle.write("You Lose!", True, align="center")
screen.exitonclick()
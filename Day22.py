# PONG game
'''
the scoreboard is a class
-> take the scores for each player
-> updates and displays the score
-> shows game over 

each paddle is a class (extend turtle)
-> fixed size
-> restrict movement to up and down
-> add event handler for player's side
-> cap movement speed
-> checkcollision
the ball is a class extend (turtle)
-> direction / angle / heading()
-> speed
-> bounce (takes the direction of the paddle that hit it/
and goes on that side)
'''
from turtle import Turtle, Screen
from Day22_ball import Ball
from Day22_dashed_line import DashedLine
from Day22_paddle import Paddle
import random
from time import sleep

from Day22_scoreboard import Scoreboard

speed = 0.01
def check_win(ball, p1, p2, scoreboard):
    px, py = ball.position()
    px1, py1 = p1.position()
    px2, py2 = p2.position()
    global speed
    if px-20 <= px1:
        if abs(py1-py)>60:
        # temp = Turtle()
        # temp.color("white")
        # temp.hideturtle()
        # temp.pu()
        # temp.write("Player 2 wins", align="center", font=('arial', 20, 'bold'))
            scoreboard.p2_wins()
            ball.movespeed = 5
            return True
        else:
            ball.movespeed += 1
    elif px+20 >= px2:
        if abs(py2-py)>60:
            # temp = Turtle()
        # temp.color("white")
        # temp.hideturtle()
        # temp.pu()
        # temp.write("Player 2 wins", align="center", font=('arial', 20, 'bold'))
            scoreboard.p1_wins()
            ball.movespeed = 5
            return True
        else:
            ball.movespeed +=1
    return False
    
    
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
DashedLine()
ball = Ball((random.randint(-330, 330),random.randint(-220, 220)), random.randint(0, 359))
p1 = Paddle((-350, random.randint(-230, 230)))
p2 = Paddle((350, random.randint(-230, 230)))
scoreboard =Scoreboard()
screen.onkeypress(p1.up, 'w')
screen.onkeypress(p1.down, 's')
screen.onkeypress(p2.up, 'Up')
screen.onkeypress(p2.down, 'Down')

game_over = False
while not game_over:
    screen.update()
    ball.move()
    sleep(0.001)
    if check_win(ball, p1, p2, scoreboard):
        ball.goto(0,0)
        
    
    
screen.exitonclick()
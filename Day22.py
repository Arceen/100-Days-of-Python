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


def check_collision(ball, p1, p2):
    px, py = ball.position()
    pass
    
screen = Screen()
screen.tracer(0)
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
DashedLine()
ball = Ball((random.randint(-430, 430),random.randint(-220, 220)), random.randint(0, 359))
p1 = Paddle((-440, random.randint(-230, 230)))
p2 = Paddle((440, random.randint(-230, 230)))

screen.onkeypress(p1.up, 'w')
screen.onkeypress(p1.down, 's')
screen.onkeypress(p2.up, 'Up')
screen.onkeypress(p2.down, 'Down')

game_over = False
while not game_over:
    screen.update()
    sleep(0.01)
    ball.move()
    if check_collision(ball, p1, p2):
        pass
screen.exitonclick()
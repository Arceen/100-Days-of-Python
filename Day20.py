# snake game 1
from Day20_snake import Snake
from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.right, 'd')
screen.listen()
game_is_on = True
while game_is_on:
    # back = snake_body.pop(0)
    # back.goto(snake_body[-1].xcor() + 20, back.ycor())
    # snake_body.append(back)
    
    screen.update()
    time.sleep(0.1)
    snake.move()
    # print(snake_body[i].position())
    # game_is_on = False
screen.exitonclick()
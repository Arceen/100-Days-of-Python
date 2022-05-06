# snake game 1
from Day20_snake import Snake
from turtle import Turtle, Screen
from Day21_food import Food
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = 0
high_score = 0
with open('Day20_data.txt') as f:
    sc = f.read()
    print(sc)
    high_score = int(sc)
score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.color("white")
score_turtle.pu()
score_turtle.goto(0, 260)
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.right, 'd')
screen.listen()
score_turtle.write(f"High Score: {high_score}. Score: {score}.", False, "center", ("courier", 15, "normal"))
game_is_on = True
while game_is_on:
    # back = snake_body.pop(0)
    # back.goto(snake_body[-1].xcor() + 20, back.ycor())
    # snake_body.append(back)
    screen.update()
    time.sleep(0.1-score*0.01)
    game_is_on = snake.move()
    if snake.head.distance(food) < 15:
        score+=1
        snake.eaten()
        food.new_food(snake.covered_positions())
        score_turtle.clear()
        score_turtle.write(f"High Score: {high_score}. Score: {score}.", False, "center", ("courier", 15, "normal"))
    if not game_is_on:
        # game ended
        print("comes here")
        if high_score < score:
            with open("Day20_data.txt", "w") as f:
                f.write(str(score))
            high_score = score
        score = 0
        score_turtle.clear()
        score_turtle.write(f"High Score: {high_score}. Score: {score}.", False, "center", ("courier", 15, "normal"))
        snake.reset()
        game_is_on = True
        
            
    
score_turtle.goto(0,0)
score_turtle.write(f"Game Over!", True, "center", ("courier", 15, "normal"))
screen.exitonclick()
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        
    def race_finished(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset(self):
        self.goto(STARTING_POSITION)
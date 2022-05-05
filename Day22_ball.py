from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self, pos, dir):
        super().__init__()
        self.pu()
        self.tilt(90)
        self.speed('fastest')
        self.shape("square")
        self.shapesize(1,1)
        self.color("white")
        self.goto(pos)
        self.setheading(dir)

    def move(self):
        self.forward(5)
        self.tilt = 0
        print(self.tiltangle())
        px, py = self.position()
        if px >= 440 or px <= -440:
            self.bounce()
        elif py >= 280 or py <= -280:
            self.bounce()
            
    def bounce(self):
        # self.rt(self.heading()%90)
        self.change_direction((self.heading()+90)%360)
        
    def change_direction(self, dir):
        self.setheading(dir)
        
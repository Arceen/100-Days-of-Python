from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self, pos, dir):
        super().__init__()
        self.pu()
        self.tilt(-90)
        self.speed('fastest')
        self.shape("circle")
        self.color("white")
        self.goto(pos)
        self.setheading(135)
        self.movespeed = 5

    def move(self): 
        self.forward(self.movespeed)
        px, py = self.position()
        if px >= 330 or px <= -330:
            self.bounce_horizontal()
        elif py >= 280 or py <= -280:
            self.bounce_vertical()
    
    def bounce_vertical(self):
        curr = self.heading()
        if curr % 90 == 0:
            self.setheading(random.randint(30, 40))
        else:
            self.setheading(360 - curr + random.randint(0,3))
        print(self.heading())
        
    def bounce_horizontal(self):
        # attempt 2
        # self.rt(self.heading()%90)
        # Attempt 1
        # self.change_direction((self.heading()+90)%360)
        # attempt 3
        curr = self.heading()
        
        if curr % 90 == 0:
            self.setheading(random.randint(30, 40))
        else:
            self.setheading(540-curr+random.randint(0,3))
        print(self.heading())
    
    def change_direction(self, dir):
        self.setheading(dir)
        
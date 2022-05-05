from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.speed('fastest')
        self.shapesize(3, 0.7)
        self.color("white")
        self.pu()
        self.goto(pos)
    def up(self):
        if self.ycor()+10<=230:
            self.goto(self.xcor(), self.ycor()+10)
    def down(self):
        if self.ycor()-10>=-230:
            self.goto(self.xcor(), self.ycor()-10)
    
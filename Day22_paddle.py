from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.pu()
        self.goto(pos)
    def up(self):
        if self.ycor()+20<=250:
            self.goto(self.xcor(), self.ycor()+20)
    def down(self):
        if self.ycor()-20>=-250:
            self.goto(self.xcor(), self.ycor()-20)
    
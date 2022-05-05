from turtle import Turtle
dashed_lines_count = 30
class DashedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.speed('fastest')
        self.color("white")
        self.width(4)
        self.hideturtle()
        self.setheading(90)
        self.goto(0, -280)
        for _ in range(dashed_lines_count):
            self.pd()
            self.forward(560//dashed_lines_count-5)
            self.pu()
            self.goto(0, self.ycor()+5)
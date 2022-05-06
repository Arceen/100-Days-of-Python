from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_score()
    
    def p1_wins(self):
        self.p1_score+=1
        self.update_score()
    
    def p2_wins(self):
        self.p2_score+=1
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Courier", 70, "normal"))
    
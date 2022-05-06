from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.pu()
        self.goto(-270, 260)
        self.hideturtle()
        self.level = 0
        
    
    def update_level_text(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

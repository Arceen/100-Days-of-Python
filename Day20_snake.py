from turtle import Turtle
MOVE_DISTANCE = 22
dir_dict = {
    "UP" : 90,
    "LEFT": 180,
    "RIGHT": 0,
    "DOWN": 270
}
class Snake:
    def __init__(self):
        pos = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_body = []
        for i in range(len(pos)):
            t = Turtle(shape="square")
            t.color("white")
            t.pu()
            t.goto(pos[i])
            self.snake_body.append(t)
            self.head = self.snake_body[0]
            
    def move(self):
        for i in range(len(self.snake_body)-1, 0,-1):
            self.snake_body[i].goto(self.snake_body[i-1].position())
        self.snake_body[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != dir_dict["DOWN"]:
            self.head.setheading(dir_dict["UP"])
        
    def down(self):
        if self.head.heading() != dir_dict["UP"]:
            self.head.setheading(dir_dict["DOWN"])
        
    def left(self):
        if self.head.heading() != dir_dict["RIGHT"]:
            self.head.setheading(dir_dict["LEFT"])
        
    def right(self):
        if self.head.heading() != dir_dict["LEFT"]:
            self.head.setheading(dir_dict["RIGHT"])
    
        
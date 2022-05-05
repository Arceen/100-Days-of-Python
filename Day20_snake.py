from turtle import Turtle
MOVE_DISTANCE = 20
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
        self.not_update_dir = True
        for i in range(len(pos)):
            t = Turtle(shape="square")
            t.color("white")
            t.pu()
            t.goto(pos[i])
            self.snake_body.append(t)
            self.head = self.snake_body[0]
    
    def tail(self):
        return self.snake_body[-1]
    def eaten(self):
        t = Turtle(shape="square")
        t.color("white")
        t.pu()
        t.goto(self.tail().position())
        self.snake_body.append(t)        
    def no_collision(self):
        for i in self.snake_body[1:]:
            if self.head.distance(i.position()) < 10:
                return False
        return True
    def covered_positions(self):
        return [x.position() for x in self.snake_body]
    def move(self):
        if -280>self.head.position()[0] or self.head.position()[0]>280 or -280>self.head.position()[1] or self.head.position()[1]>280:
            return False
        for i in range(len(self.snake_body)-1, 0,-1):
            self.snake_body[i].goto(self.snake_body[i-1].position())
        self.snake_body[0].forward(MOVE_DISTANCE)
        self.not_update_dir = True
        return self.no_collision()
    def head_pos(self):
        return self.head.position()
    def up(self):
        if self.not_update_dir and self.head.heading() != dir_dict["DOWN"]:
            self.head.setheading(dir_dict["UP"])
            self.not_update_dir = False
        
    def down(self):
        if self.not_update_dir and self.head.heading() != dir_dict["UP"]:
            self.head.setheading(dir_dict["DOWN"])
            self.not_update_dir = False
        
    def left(self):
        if self.not_update_dir and self.head.heading() != dir_dict["RIGHT"]:
            self.head.setheading(dir_dict["LEFT"])
            self.not_update_dir = False
        
    def right(self):
        if self.not_update_dir and self.head.heading() != dir_dict["LEFT"]:
            self.head.setheading(dir_dict["RIGHT"])
            self.not_update_dir = False

        
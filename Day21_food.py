from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        rx, ry = random.randint(-14, 14)*20, random.randint(-14, 14)*20
        self.goto((rx, ry))
    
    def new_food(self, snake_positions):
        rx, ry = random.randint(-14, 14)*20, random.randint(-14, 14)*20
        while (rx,ry) in snake_positions:
            rx, ry = random.randint(-14, 14)*20, random.randint(-14, 14)*20
        self.goto((rx, ry))
        
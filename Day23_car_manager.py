from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

class Car(Turtle):
    def __init__(self, color, pos, ms):
        super().__init__()
        self.color(color)
        self.pu()        
        self.goto(pos)
        self.shape('square')
        self.shapesize(1, 2)
        self.lt(180)
        self.dist = ms
        
    def drive(self):
        self.fd(self.dist)
    
    def remove(self):
        self.clear()
        self.hideturtle()
class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.chances_in_hundred = 10
    
    def has_collided(self, t):
        for car in self.car_list:
            if abs(car.xcor()-t.xcor()) < 15:
                if car.ycor()-10 < t.ycor()+15 < car.ycor()+10 or car.ycor()-10 < t.ycor()-10 < car.ycor()+10:
                    return True
        return False
        
    def random_car_generator(self):
        if random.randint(1, 100)<self.chances_in_hundred:
            self.car_list.append(self.generate_car())
    
    def move_all_cars_forward(self):
        for car in self.car_list:
            if car.xcor() < -SCREEN_WIDTH//2 - 20:
                self.car_list.remove(car)
                
            else:
                car.drive()
    
    def generate_car(self):
        color = random.choice(COLORS)
        pos = (SCREEN_WIDTH//2+40, random.randint(-SCREEN_HEIGHT//2+50, SCREEN_HEIGHT//2-50))
        # checking the boundaries
        # pos = (SCREEN_WIDTH//2+40, -250)
        
        return Car(color, pos, self.move_speed)
    
    def tick(self):
        self.random_car_generator()
        self.move_all_cars_forward()

    def next_level(self):
        for car in self.car_list:
            car.remove()
            del car
        self.car_list = []
        self.move_speed += MOVE_INCREMENT/20
        self.chances_in_hundred += 2
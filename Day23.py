# The turtle crossing capstone project

import time
from turtle import Screen, Turtle
from Day23_player import Player
from Day23_car_manager import CarManager
from Day23_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.go_up, 'Up')

screen.listen()
game_is_on = True
scoreboard = Scoreboard()
scoreboard.update_level_text()
while game_is_on:
    time.sleep(0.01)
    carmanager.tick()
    if carmanager.has_collided(player):
        break
    finished_level = player.race_finished()
    if finished_level:
        player.reset()
        scoreboard.update_level_text()
        carmanager.next_level()
    screen.update()

game_over_turtle = Turtle()
game_over_turtle.pu()
game_over_turtle.write("Game Over!", align="center", move = False, font = ("Courier", 22, "normal"))

screen.exitonclick()
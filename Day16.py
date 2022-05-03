# Day 16 OOP

# Model Waiter
# is_holding_plate = True
# tables_responsible = [4,5,6]
# def take_order (table, order):
# takes order
# def take_payment (table, amount):
# process payment

# class is a blueprint
# object is the actual architecture
from math import sin, cos, pi
from turtle import Screen, Turtle
from prettytable import PrettyTable
# color('red', 'yellow')
# begin_fill()
# # TODO: Create a sun
# while True:
#     forward(300)
#     left(170)
#     if (abs(pos())) < 1:
#         break


# Bangladeshi flag (w/o pole)
#
# sides = 4
# color('black', 'green')
# penup()
# setposition(-125, -40)
# pendown()
# begin_fill()
# for i in range(sides):
#     forward(250 if i%2 == 0 else 150)
#     left(360//sides)
#     if (abs(pos())) < 1:
#         break
# end_fill()
# penup()
# setposition(0, 0)
# pendown()
# # TODO: Any - agon
# use higher equal sided polygons to give feel of a circle
# sides = 40
# color('black', 'red')
# begin_fill()
# for _ in range(sides):
#     forward(5)
#     left(360//sides)
#     if (abs(pos())) < 1:
#         break
#
# end_fill()

# Waving Flag
# color("black", "blue")
#
# wave_height = 20
# dist = 200
# waves can be a fraction too
# waves = 0.75
# cycle_length = dist/waves

'''
dist = 0
cycle_length = 50

0 49 100
'''
# begin_fill()
# for i in range(dist):
#     # change y based on sin
#     cal_y = round(wave_height * sin((360*i/cycle_length)*pi/180), 2)
#     setpos(i, cal_y)
# end_fill()
# done()

# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("darkgreen")
# my_turtle.forward(100)
# my_screen = my_turtle.getscreen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
# x = PrettyTable()
# x.field_names = ["Name", "Age"]
# x.add_rows([
#     ["Angela", "13"],
#     ["Aladdin", "17"],
#     ["Ariel", "16"]
# ])
#
# x.title = "Ages"
# print(x)
#
# print(x.fields)
# y = PrettyTable()
# y.add_column("Names", ["Washington", "Jefferson", "Howls", "Hughes", "Bush", "Obama", "Trump", "Biden"])
# print(y)
# pokemon_table = PrettyTable()
# pokemon_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasor"])
# pokemon_table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
# pokemon_table.align = 'l'
# print(pokemon_table)

from Day16_menu import Menu
from Day16_coffee_maker import CoffeeMaker
from Day16_money_machine import MoneyMachine

curr_menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
while True:
    choice = input(f"What would you like? ({curr_menu.get_items()[:-1]}): ")
    if choice == 'off':
        break
    elif choice == 'report':
        coffeemaker.report()
    else:
        drink = curr_menu.find_drink(choice)
        if drink == None:
            continue
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)


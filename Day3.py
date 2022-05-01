# Day 3 - Conditinal Statements, Logical Operators, Code blocks and Scope

# Exercise 3.1 - Odd or Even
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# Exercise 3.2 - BMI Calculator 2.0
# weight = float(input("Enter your weight(kg): "))
# height = float(input("Enter your height(m): "))
# bmi = round((weight)/(height**2),2)
# if bmi < 18.5:
#     situation = "Underweight"
# elif bmi < 25:
#     situation = "of Normal Weight"
# elif bmi < 30:
#     situation = "Overweight"
# elif bmi < 35:
#     situation = "Obese"
# else:
#     situation = "Clinically Obese"
# print(f"Your BMI is {bmi}, and you are {situation}")

#Exercise 3.3 - Leap Year
# year = int(input("Which year you want to check? "))
# if year % 400 == 0:
#     print("Leap Year")
# elif year % 4 == 0:
#     if year % 100 == 0:
#         print("Not a Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Normal Year")

#Exercise 3.4 - Pizza Order Exercise
# print("Welcome to Python Pizza Delilveries!")
# size = input("What size pizza do you want? (S, M, or L) ")
# add_pepperoni = input("Do you want pepperoni? (Y or N) ")
# extra_cheese = input("Do you want extra cheesse? (Y or N) ")

# bill = 0
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == 'Y':
#     bill += 1

# print(f"Your final bill is: ${bill}")

# Exercise 3.5 - Love Calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# true_no = 0
# love_no = 0
# name = name1.lower()+name2.lower()
# true_no += name.count('t')
# true_no += name.count('r')
# true_no += name.count('u')
# true_no += name.count('e')
# love_no += name.count('l')
# love_no += name.count('o')
# love_no += name.count('v')
# love_no += name.count('e')
# true_love = int(str(true_no)+str(love_no))

# if 10 > true_love > 90:
#     print(f"Your score is {true_love}, you goo together like coke and mentos")
# elif true_love<=50 and true_love>=40:
#     print(f"Your score is {true_love}, you are alright together.")
# else:
#     print(f"Your score is {true_love}")

# Day 3 Project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"")
choice1 = input().lower()
if choice1 != "left":
    print("You fell into a hole. Game Over.")
else:
    print("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    choice2 = input().lower()
    if choice2 != "wait":
        print("Attacked by trout. Game Over")
    else:
        print("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color door do you choose?")
        choice3 = input().lower()
        if choice3 == "red":
            print("Burned by fire. Game Over")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over")
        elif choice3 != "yellow":
            print("Went YOLO. Game Over")
        else:
            print("You found the treasure! You Win!")
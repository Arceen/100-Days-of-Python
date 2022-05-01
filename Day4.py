import random
# Day 4 - Randomisation and lists
# random_integer = random.randint(1,2)
# print(random_integer)
# random_float = random.random()
# print(random_float*5+random_float*0.1)
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# Exercise 4.1 - Coin toss
# choices = ["Heads", "Tails"]
# print(random.choice(choices))
# choice_index = random.randint(0,1)
# print(choices[choice_index])

# some_numbers = [12, 1, 6,52, 52, 123,57]
# some_numbers.extend([123,5,67,8,-10])
# print(some_numbers)

# Exercise 4.2 - 
# names = input("Enter the names of people: ").split(", ")
# print(names[random.randint(0, len(names)-1)]+ " is going to pay for everyone's meals")

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Exercise 4.3
# row1 = ["😄", "😍", "🥌"]
# row2 = ["🐵", "♨️", "🏐"]
# row3 = ["👁️","🐴", "💢"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# map[int(position[1])-1][int(position[0])-1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")

# Day 4 Exercise
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

show_ascii = [rock, paper, scissors]
print("Welcome to Rock, Papers, Scissors game. Type 0 for Rock, 1 for Paper or 2 for Scissors")
user_choice = int(input())
computer_choice = random.randint(0,2)
print("You chose: ")
print(show_ascii[user_choice])
print("Computer chose: ")
print(show_ascii[computer_choice])
if user_choice == computer_choice:
    print("Draw")
else:
    if user_choice == 0:
        if computer_choice == 1:
            print("You Lose!")
        else:
            print("You Win!")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You Win!")
        else:
            print("You Lose!")
    else:
        if computer_choice == 1:
            print("You Win!")
        else:
            print("You Lose!")


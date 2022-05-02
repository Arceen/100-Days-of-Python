# Day 14 Project Higher or Lower

# TODO 0: Create necesssary modules with data and import them
import random
from os import system
from Day14_art import logo, vs
from Day14_gamedata import data

# TODO 1: Create a function that games
def higher_lower_game():
    # TODO 3: print the game logo
    my_data = data[:]
    score = 0
    random.shuffle(my_data)
    while score<len(my_data)-1:
        # print logo every single time
        print(logo)
        if score != 0:
            print(f"You're right! Current score: {score}.")
        # 'follower_count': 346,
        # 'description': 'Social media platform',
        # 'country': 'United States'
        a = my_data[score]
        b = my_data[score+1]
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        if input("Who has more followers? Type 'A' or 'B': ")=='A':
            if a["follower_count"] < b["follower_count"]:
                system('cls')
                print(logo)
                print(f"You lost! Your score was: {score}")
                return
        else:
            if a["follower_count"] > b["follower_count"]:
                system('cls')
                print(logo)
                print(f"You lost! Your score was: {score}")
                return
               
        # if user was right we are going to go to the next
        score += 1
        # clear the screen
        system('cls')



# TODO 2: Call the game function
higher_lower_game()
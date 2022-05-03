# Day 12 Scope

# local scope
# enemies = 1
# def increase_enemies():
#     # creates a local variable enemies with value 2
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies outside function: {enemies}")
    
# player_health = 10

# def game():
#     # local scope function
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()

# game()

# no block scope (variables created inside if blocks are not considered to be inside if, rather on the level before if)
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Beasts"]
# if game_level > 1:
#     # this is accessible from the previous block
#     new_enemy = "Werewolves"
# print(new_enemy)

# Modifying Global scope
# enemies = 0
# def increase_enemies():
#     # not recommended
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# enemies = 0
# def increase_enemies():
#     return enemies+1
# enemies = increase_enemies()

# Global constants
# PI = 3.141592
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@yu_me_dem"

# Day 12 - Final Project

from Day12_art import logo
import random
def number_guesser_game():
    number = random.randint(1,100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # print(f"Pssst, the answer is {number}")
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'hard':
        num_of_attempts = 5
    else:
        num_of_attempts = 10
    
    while num_of_attempts > 0:
        print(f"You have {num_of_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {guess}.")
            return
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
        num_of_attempts -= 1
        if num_of_attempts != 0:
            print("Guess again.")
            
    print("You've run out of guesses. You lose!")
    print(f"The answer was {number}.")
    
number_guesser_game()
# Day 7 - For/While loops, if/else, range, modules, lists
import random

# Exercise 7.1 - Hangman Start

# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# guessed_letter = input("Guess a letter: ")
# if guessed_letter.lower() in chosen_word.lower():
#     print("Correct Guess")
# else:
#     print("Incorrect guess")

# Exercise 7.2

# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# print("The chosen word was: " + chosen_word)
# display = ['_' for _ in chosen_word]
# guess = input("Guess a letter: ").lower()
# for i in range(len(chosen_word)):
#     if guess == chosen_word[i]:
#         display[i] = chosen_word[i] 
# print(display)

# Exercise 7.3

# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# print("The chosen word was: " + chosen_word)
# display = ['_' for _ in chosen_word]
# while '_' in display:
#     guess = input("Guess a letter: ").lower()
#     for i in range(len(chosen_word)):
#         if guess == chosen_word[i]:
#             display[i] = chosen_word[i] 
#     print(display)
# print("You win")

# Exercise 7.4

# lives = 6
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# print("The chosen word was: " + chosen_word)
# display = ['_' for _ in chosen_word]
# while '_' in display and lives>0:
#     guess = input("Guess a letter: ").lower()
#     correct = False
#     for i in range(len(chosen_word)):
#         if guess == chosen_word[i]:
#             display[i] = chosen_word[i]
#             correct = True
#     if not correct:
#         lives -= 1
#     print(display)
# if lives > 0:
#     print("You win")
# else:
#     print("You lose")

# Exercise 7.5 - Improving UX
# import Day7_hangman_art
# print(Day7_hangman_art.ascii)
# from Day7_hangman_word import word_list
# from Day7_hangman_word import *
# lives = 6
# chosen_word = random.choice(word_list)
# print("The chosen word was: " + chosen_word)
# display = ['_' for _ in chosen_word]
# while '_' in display and lives>0:
#     guess = input("Guess a letter: ").lower()
#     correct = False
#     for i in range(len(chosen_word)):
#         if guess == chosen_word[i]:
#             display[i] = chosen_word[i]
#             correct = True
#     if not correct:
#         lives -= 1
#     print(display)
# if lives > 0:
#     print("You win")
# else:
#     print("You lose")


# Day 7 Project - Hangman

# hangman_pics = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']


# ascii = '''
#  _   _                                         
# | | | |                                        
# | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
# |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/                       
# '''
# #Word bank of animals
# word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
#          'coyote crow deer dog donkey duck eagle ferret fox frog goat '
#          'goose hawk lion lizard llama mole monkey moose mouse mule newt '
#          'otter owl panda parrot pigeon python rabbit ram rat raven '
#          'rhino salmon seal shark sheep skunk sloth snake spider '
#          'stork swan tiger toad trout turkey turtle weasel whale wolf '
#          'wombat zebra ').split()


# from Day7_hangman_word import word_list
# from Day7_hangman_art import *
# def pick_a_word():
#     return random.choice(word_list)

# def welcome():
#     print(ascii)

# def show_picked(letter_state):
#     for letter in letter_state:
#         print(letter, end=" ")
#     print("")

# def prompt_pick():
#     return input('Guess a letter: ')

# def altered_letter_state(picked_letter, curr_word, letter_state):
#     for i in range(len(curr_word)):
#         if curr_word[i] == picked_letter.upper() or curr_word[i] == picked_letter.lower():
#             letter_state[i] = curr_word[i] 
#     return letter_state


# def start_game():
#     curr_word = pick_a_word()
#     already_picked = []
#     letter_state = ['_' for _ in range(len(curr_word))]
#     welcome()
#     number_of_guesses = 0
#     while number_of_guesses < 6:
#         show_picked(letter_state)
#         print("")
#         picked_letter = prompt_pick()
#         print("")
#         if picked_letter in already_picked:
#             print("You have already picked that letter. Pick another one.")
#             print("")
#             continue
#         already_picked.append(picked_letter)
#         if picked_letter in curr_word:
#             letter_state = altered_letter_state(picked_letter, curr_word, letter_state)
#             if '_' not in letter_state:
#                 print("🥳 🥳 🥳 You Won! 🥳 🥳 🥳 ")
#                 return
#             else:
#                 print("😊 Correct Guess! 😊 ")
#                 print("")
#         else:
#             print("😥 You guessed " + picked_letter+ " which is not in the word. 😥" )
#             print("")
#             number_of_guesses += 1
#         print(hangman_pics[number_of_guesses])
#         print("")
#     print(f"The word was {curr_word}!")
#     print("😭😭😭 Game Over! You Lost! 😭😭😭")
# start_game()




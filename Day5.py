import random
# Day 5 - Lists, Loops

# List Iteration
# fruits = ["Apple", "Peach", "Strawberry"]
# for i in fruits:
#     print(i+" pie")

# Exercise 5.1 - Average Height
# heights = list(map(int, input().strip().split(" ")))
# sum_heights = 0
# for i in heights:
#     sum_heights += i
# print(round(sum_heights/len(heights)))

# Exercise 5.2 - Highest Score
# scores = list(map(int, input().strip().split(" ")))
# highest_score = 0
# for score in scores:
#     if score > highest_score:
#         highest_score = score
# print(highest_score)

# loop range + step
# for i in range(1, 100, 4):
#     print(i)

# Exercise 5.3 - Adding Evens Exercise
# total = 0
# for i in range(2, 101, 2):
#     total+=i
# print(total)

# Exercise 5.4 - FizzBuzz
for i in range(1, 101):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%7 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)

# Day 5 project
# print("Welcome to the PyPassword Generator!")
# print("How many letters would you like in your password?")
# letter_count = int(input())
# print("How many symbols would you like?")
# symbol_count = int(input())
# print("How many numbers would you like?")
# number_count = int(input())
# password = ""
# small = [ chr(97+i) for i in range(26) ]
# cap = [ chr(65+i) for i in range(26) ]
# letters = small + cap
# symbols = ["!", "@","#","$","%","^","&","*","(",")","-","=","/",".","~"]
# for i in range(letter_count):
#     password += letters[random.randint(0, len(letters)-1)]
# for i in range(symbol_count):
#     password += symbols[random.randint(0, len(symbols)-1)]
# for i in range(number_count):
#     password += str(random.randint(0,9))
# print(password)
# password = list(password)
# random.shuffle(password)
# new_password = ''.join(password)
# print(new_password)
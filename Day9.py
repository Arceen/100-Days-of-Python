# Day 9 - dictionaries, list, auction program

# Exercises 9.1 Grading porgram

# students_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# students_grades = {}

# for i in students_scores:
#     if students_scores[i]<70:
#         students_grades[i] = "Fail"
#     elif students_scores[i]<=80:
#         students_grades[i] = "Acceptable"
#     elif students_scores[i]<=90:
#         students_grades[i] = "Exceeds Expectations"
#     elif students_scores[i]<=100:
#         students_grades[i] = "Outstanding"

# print(students_grades)

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }
# # Nesting Lists inside Dictionary
# travel_log = {
#     "France": ["Paris", "Little", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }
# # Nesting Dictionaries inside dictionaries
# travel_log_dict = {
#     "France": {"visited_cities": ["Paris", "Little", "Dijon"]},
#     "Germany": {"visited_cities": ["Berlin", "Hamburg", "Stuttgart"]}
# }
# print(travel_log_dict)
# # Nesting Dictionaries inside list
# travel_log_list = [
#     {"country": "France", "cities": ["Paris", "Little", "Dijon"], "times visited": 2},
#     {"country": "Germany","cities":["Berlin", "Stuttgart", "Hamburg"], "time visited":2}
# ]

# Exercise 9.2 Dictionary inside list 

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Little", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 7,
#         "cities": ["Berlin", "Hamburg", "Stuttsgart"]
#     },
# ]


# def add_new_country(country, visits, cities):
#     travel_log.append({
#         "country": country,
#         "visits": visits,
#         "cities": cities,
#     })

# add_new_country("Russia", 3, ["Moscow", "Saint Petersburg", ])
# print(travel_log)


from os import system
from Day9_art import logo

# Non dict approach
def sealed_secred_bid_auction_non_dict():
    print(logo)
    print("Welcome to the secret auction program")
    winner_name = ""
    winner_bid = 0
    while True:
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        if bid > winner_bid:
            winner_bid = bid
            winner_name = name
        print("Are there any other bidders? Type 'yes' or 'no'.")
        choice = input().lower()
        if choice != 'yes':
            print(f"{winner_name} wins the item with the bid of ${winner_bid}")
            return
        system('cls')

def sealed_secred_bid_auction():
    print(logo)
    print("Welcome to the secret auction program")
    bid_dict = {}
    while True:
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        bid_dict[name] = bid
        print("Are there any other bidders? Type 'yes' or 'no'.")
        choice = input().lower()
        if choice != 'yes':
            winner_name = ""
            winner_bid = 0
            for name in bid_dict:
                if bid_dict[name] > winner_bid:
                    winner_bid = bid_dict[name]
                    winner_name = name
                
            print(f"{winner_name} wins the item with the bid of ${winner_bid}")
            return
        system('cls')


sealed_secred_bid_auction()
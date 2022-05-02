# Day 10 calculator, output functions, docstrings


# functions with outputs
# def format_name(f_name, l_name):
#     print(f"{f_name.title()} {l_name.title()}")
# format_name("nIlOy", "hasaN")

# empty input
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         print("You didn't enter anything")
#         return
#     print(f"{f_name.title()} {l_name.title()}")
# format_name("", "")

# Days in month
# resuing from 3.3
# def is_leap(year):
#     if year % 400 == 0:
#         return True
#     elif year % 4 == 0:
#         if year % 100 == 0:
#             return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     if 0>month or month>11:
#         print("Incorrect Input")
#         return -1
        
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 1:
#         return month_days[month] + is_leap(year)
#     return month_days[month]
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month-1)
# print(days)

# functions with outputs
# def format_name(f_name, l_name):
#     print(f"{f_name.title()} {l_name.title()}")
# format_name("nIlOy", "hasaN")

# docstrings 
# def format_name(f_name, l_name):
#     """
#     Take a first_name and last name and format it to return the title case version of the name
#     """
#     if f_name == "" or l_name == "":
#         print("You didn't enter anything")
#         return
#     print(f"{f_name.title()} {l_name.title()}")
# format_name("", "")


# Day 10 project - Calculator
from Day10_art import logo
def add(x, y):
    print(f"{x} + {y} = {round(x+y,2)}")
    return round(x+y,2)
def sub(x,y):
    print(f"{x} - {y} = {round(x-y,2)}")
    return x-y
def mul(x,y):
    print(f"{x} * {y} = {round(x*y,2)}")
    return round(x*y,2)
def div(x,y):
    if y == 0:
        print("Can't divide by zero")
        return 0
    print(f"{x} / {y} = {round(x/y, 2)}")
    return round(x/y, 2)

def calculator():
    print(logo)
    op_dict = {'+': add, '-': sub, '*': mul, '/':div}
    x = y = None
    while True:
        if x == None:
            x = float(input("What's the first number? "))
        for op in op_dict:
            print(op)
        op = input("Pick an operation: ")
        y = float(input("What's the second number?: "))
        x = op_dict[op](x,y)
        choice = input(f"Type 'y' to continue calculating with {x}, or type 'n' to start a new calculation: ")
        if choice == 'n':
            x = y = None
        elif choice != 'y':
            return

calculator()
    
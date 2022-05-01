# Day 2 - Data Types, Numbers, Operations, Type Conversions, f-Strings

# type check
# print(type(2))

# type conversion/casting
# int("123")
# str(123)
# float(123)

# Ex 1.1 - Add digits of 2 digit number
# num = input("Enter a number: ")
# print("The sum of the digits is: "+str(int(num[0])+int(num[1])))

# PEMDASLR
# ()
# **
# * /
# + -
# Left to Right

# Exercise 2.2
# weight = float(input("Enter your weight(kg): "))
# height = float(input("Enter your height(m): "))
# print("Your BMI(Body Mass Index) is: "+str(round((weight)/(height**2),2)))

# Float Precision
# Can round a float
# round(2.6)
# Can round to a fixed precision
# round(2.6134, 2)

# Exercise 2.3 - Your life in weeks
# age = int(input("What is your age? "))
# years_left = (90-age)
# print(f"You have {years_left*365} days, {years_left*52} weeks, and {years_left*12} months left.")

# Day 2 Project
# print("Welcome to the tip calculator.")
# total_bill = float(input("What was the total bill? $"))
# total_people = int(input("How many people to split the bill? "))
# tip_percentage = int(input("What percentage(%) tip would you like to give? 10, 12 or 15? "))
# print(f"Each person should pay: $ {(total_bill*((100+tip_percentage)/100))/total_people}")

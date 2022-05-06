# list comprehension and dictionary comprehension
# my_nums = [1,2,3]
# new_nums = [i+1 for i in my_nums]
# print(new_nums)
# letters_list = [letter for letter in 'niloy']
# print(letters_list)
# print([i*2 for i in range(1,5)])
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# print([name.upper() for name in names if len(name)>5])
# numbers = [1,1,2,3,5,8,13,21,34, 55]
# print([i*i for i in numbers])
# print([i for i in numbers if not i%2])
# with open("Day26_file1.txt") as f1:
#     nums1 = [int(i) for i in f1.readlines()]
# with open("Day26_file2.txt") as f2:
#     nums2 = [int(i) for i in f2.readlines()]
# print([i for i in nums1 if i in nums2])
# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave']
# student_scores = {name: random.randint(1,100) for name in names}
# passed_students = {name: score for (name,score) in student_scores.items() if score>40}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {i:len(i) for i in sentence.split(" ")}
# print(result)
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
# result = {day: temperature*9/5+32 for (day, temperature) in weather_c.items()}
# print(result)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# for (key,value) in student_dict.items():
#     print(value)

# import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (index, row) in student_data_frame.iterrows():
#     print(row)
import pandas
df = pandas.read_csv('Day26_nato_phonetic_alphabet.csv')
def name_phonetics():
    name = input("Enter your name: ")
    res = []
    for letter in name.upper():
        res.append(df[df.letter == letter].code.values[0])
    print(res)
name_phonetics()
my_dict = {item.letter:item.code for (index, item) in df.iterrows()}
print(my_dict)
# Day 24 - File I/O, automation, files, file path, directories

# with open('Day24_text_file1.txt', mode="a") as f:
#     f.writelines(["abcd", "a", "b", "c", "d"])

    
'''
current folder: ./this_file_is_in_same_directory.
previous folder: ../this_file_is_in_the_enclosing_directory

absolute vs relative:
absolute is relative to the root of the os
relative is relative to the current working folder
'''

# Letter automation project
# letter_for_Aang.txt
with open('./Day24_Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

with open('./Day24_Input/Names/invited_names.txt') as name_file:
    people = name_file.read().split("\n")

print(letter)
print(people)

for name in people:
    with open(f'./Day24_Output/ReadyToSend/Letter_for_{name}.txt', "w") as invite_letter:
        invitation = letter.replace("[name]", name)
        invite_letter.write(invitation)

    



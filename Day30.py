#Error handling, raising exceptions, json
# try:
#     file = open("Day281.py", "r")
# except FileNotFoundError as e:
#     print(e)
# else:
#     print("no error")
#     file.close()
# finally:
#     print("this code has finished executing")

# height = float(input())
# if height > 3:
    # raise ValueError("Human Height does not exceed 3 meters")
# fruits = ["Apple", "Pear", "Orange"]

# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit +" pie")
# try:
#     make_pie(4)
# except IndexError as e:
#     print("Fruit Pie")

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3},  
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#         pass

# print(total_likes)

# import pandas
# df = pandas.read_csv('Day26_nato_phonetic_alphabet.csv')
# phonetic_dict = {row.letter:row.code for (_, row) in df.iterrows()}
# # print(phonetic_dict)
# def name_phonetics():
#     try:
#         name = input("Enter your name: ")
#         res = []
#         for letter in name.upper():
#             res.append(phonetic_dict[letter])
#         print(res)
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         name_phonetics()
# name_phonetics()

# json.dump() json.load() json.update()

# From Day 29
from tkinter import *
from tkinter.messagebox import askokcancel, askyesno, showerror, showinfo
import random
import json
# import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search_website():
    with open("Day30_data.json", "r") as json_file:
        website = website_entry.get()
        if  website == '':
            showerror("Password Manager", "Please enter website name")
            
        # pass_file.write(' | '.join([website_entry.get(),email_entry.get(), password_entry.get()])+'\n')
        try:
            data = json.load(json_file)
            if website.lower() not in data.keys():
                showerror("Password Manager", "The website does not exist")
            else:
                if askyesno(title="Password Manager", message=f"Website: {website}\n\nEmail: {data[website.lower()]['Email']}\n\nPassword: {data[website.lower()]['Password']}\n\n\nCopy the password?"):
                    r = Tk()
                    r.withdraw()
                    r.clipboard_clear()
                    r.clipboard_append(data[website.lower()]['Password'])
                    r.update()
                    r.destroy()
                    
        except:
            showerror("Password Manager", "The website does not exist")
            print('reading json file error')
def generate_password():
    letter_count = random.randint(8,10)
    symbol_count = random.randint(4,6)
    number_count = random.randint(5,8)
    password = ""
    small = [ chr(97+i) for i in range(26) ]
    cap = [ chr(65+i) for i in range(26) ]
    letters = small + cap
    symbols = ["!", "@","#","$","%","^","&","*","(",")","-","=","/",".","~"]
    for i in range(letter_count):
        password += letters[random.randint(0, len(letters)-1)]
    for i in range(symbol_count):
        password += symbols[random.randint(0, len(symbols)-1)]
    for i in range(number_count):
        password += str(random.randint(0,9))
    password = list(password)
    random.shuffle(password)
    new_password = ''.join(password)
    # print(new_password)
    password_entry.delete(0, END)
    password_entry.insert(END, new_password)
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(new_password)
    r.update()
    r.destroy()
# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_added():
    if  website_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '':
        showerror("Password Manager", "Please fill all fields")
    elif askokcancel(title="Password Manager", message=f"Website: {website_entry.get()}\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}"):
        info = {
                website_entry.get().lower():{
                    "Email": email_entry.get(),
                    "Password": password_entry.get()
                }
            }
        with open("Day30_data.json", "r") as json_file:
            
            # pass_file.write(' | '.join([website_entry.get(),email_entry.get(), password_entry.get()])+'\n')
            try:
                prev = json.load(json_file)
                info.update(prev)
            except:
                print('No data in json yet')
        with open("Day30_data.json", "w") as json_file:
            try:
                json.dump(info, json_file, indent=4)
            except:
                print('error writing to json file')
        # print(prev["sadasd"])
        # info.update(prev)
        # json.dump(info, json_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        showinfo("Password Manager", "Password Saved")
           
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg="white")
window.minsize(height=200, width=200)

#logo
lock_logo = PhotoImage(file="Day29_logo.png") 
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(row = 0, column=1)

# labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "rapid_z00@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

#buttons
search_website_button = Button(width=15,text="Search", command=search_website)
search_website_button.grid(row=1, column=2)

generate_password_button = Button(width=15,text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, command=password_added)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
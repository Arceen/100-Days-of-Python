# Day 31 Flash Card Capstone project
from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_word_index = -1
# Base UI setup
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(width=600, height=400)

# next card
def next_word():
    global timer
    global current_word_index
    if timer:
        window.after_cancel(timer)
    if len(words) == 0:
        canvas.itemconfig(lang, text="French Expert!", fill="black")
        canvas.itemconfig(word, text="No words left!", fill="black")
        return
    current_word_index = random.randint(0, len(words)-1)
    curr_word = words[current_word_index]
    wd = curr_word[0]
    canvas.itemconfig(back_image, image=card_front)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=wd, fill="black")
    timer = window.after(1000, flipped_card, curr_word[1])
    
def flipped_card(wd):
    # show engrish word
    canvas.itemconfig(back_image, image=card_back)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=wd, fill="white")
    
def word_remembered():
    del words[current_word_index]
    save_file = pandas.DataFrame(words, columns=["French", "English"])
    save_file.to_csv('Day31_words_to_learn.csv')
    print("Successfully Updated list")
    next_word()

#get the image assets


#setup the words
try:
    data = pandas.read_csv('Day31_words_to_learn.csv').to_dict(orient='records')
    if len(data) == 0:
        raise ValueError("Read from the original")
except:
    data = pandas.read_csv('Day31_data/french_words.csv').to_dict(orient='records')

words = [[i["French"],i["English"]] for i in data]
# print(words["English"].sample().values[0])
# print(words)

card_front = PhotoImage(file="Day31_images/card_front.png")
card_back = PhotoImage(file="Day31_images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)


#buttons
check_pic = PhotoImage(file="Day31_images/right.png")
check_button = Button(image=check_pic, bd=0, highlightthickness=0, command=word_remembered)
check_button.grid(column=1, row=1)

cross_pic = PhotoImage(file="Day31_images/wrong.png")
cross_button = Button(image=cross_pic, bd=0, highlightthickness=0, command=next_word)
cross_button.grid(column=0, row=1)

lang = canvas.create_text(400, 145, text="",font=('Ariel', 30, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Ariel', 55, 'bold'))
next_word()


window.mainloop()


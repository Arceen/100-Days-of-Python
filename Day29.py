# Day 29 password manager gui with tkinter
from tkinter import *
from tkinter.messagebox import askokcancel, showerror, showinfo
import random
# import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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
    print(new_password)
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
        with open("Day29_passwords.txt", "a") as pass_file:
            pass_file.write(' | '.join([website_entry.get(),email_entry.get(), password_entry.get()])+'\n')
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
website_entry = Entry(width=54)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "rapid_z00@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

#buttons
generate_password_button = Button(width=15,text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, command=password_added)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
# Use tkinter to build gui, kwargs
# from tkinter import *
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=60, pady=60)
# # button event
# def button_clicked():
#     my_label['text'] = input.get()
    
# #Label
# my_label = Label(text="I am the boss!", font=("Arial", 24, 'bold'))
# # my_label.pack(side="left")
# # my_label.place(x=440, y= 240)
# my_label.grid(column=0, row=0)
# my_label.config(padx=20, pady=20)

# my_label['text'] = 'new text'
# my_label.config(text="a newer text")


# # button
# button = Button(text="Click me!", command=button_clicked)
# # button.pack()
# button.grid(row=1,column=1)

# new_button = Button(text="No Click me!", command=button_clicked)
# new_button.grid(row=0, column=2)

# # entry
# input = Entry(width=10)
# # input.pack()
# print(input.get())
# input.grid(row=2, column=3)
# window.mainloop()

#------------------------------------------------------

# from tkinter import *

# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)

# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()

# #Buttons
# def action():
#     print("Do something")

# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()

# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()

# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert('end', "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
#-------------------------------------------------------

# def add(*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
# print(add(1,2,34,5,6,7))

# def calculate(**kwargs):
#     print(kwargs)
# calculate(add = 3, mutilply=5)

# class MyClass:
#     def __init__(self, **kwargs):
#         self.something = kwargs.get('something')

# MyClass(nothingthing="this")


from tkinter import *


def convert():
    label4.config(text=str(round(float(entry.get())*1.6)))
    # label4.config(text=str(round(
    # int(entry.get())/1.6),2))
window = Tk()
window.title('Mile to Km converter')
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(row=0, column=1)

label = Label(text="Miles")
label.grid(row=0, column=2)
label2 = Label(text="Km")
label2.grid(row=1, column=2)
label3 = Label(text="is equal to")
label3.grid(row=1, column=0)
label4 = Label(text="0")
label4.grid(row=1, column=1)

button = Button(text="Calculate", command=convert)
button.grid(row = 2, column = 1)

window.mainloop()
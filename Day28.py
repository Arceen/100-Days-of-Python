# Day 28 pomodoro app
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECKMARK = '✓'
timer = None
timer_running = False
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global timer_running
    reps = 0
    timer_running = False
    window.after_cancel(timer)
    timer_head_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    time = LONG_BREAK_MIN if reps%8 == 0 else WORK_MIN if reps%2==1 else SHORT_BREAK_MIN
    timer_head_label.config(text="Work" if reps%2 else "Break", fg = RED if reps%8 == 0 else GREEN if reps%2==1 else PINK)
    
    count_down(time * 60)
    
def start_button_pressed():
    global timer_running
    if timer_running:
        return
    else:
        timer_running=True
        start_timer()
#button Events
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count < 0:
        checkmarks.config(text=CHECKMARK*((reps+1)//2))
        start_timer()
        return
    else:
        global timer
        minutes, seconds = count//60, count%60
        minutes, seconds = f"{minutes//10}{minutes%10}", f"{seconds//10}{seconds%10}"
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        timer = window.after(1000, count_down, count-1)
    

# ---------------------------- UI SETUP ------------------------------- #

        
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

    
#tomato image
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='Day28_tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


#timer label
timer_head_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
timer_head_label.grid(row=0,column=1)

#start button
start_button = Button(text="Start", command=start_button_pressed, highlightthickness=0)
start_button.grid(row=2, column=0)

#reset button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

#ticks label
checkmarks = Label(text='', fg=GREEN, font=(FONT_NAME, 15, "normal"), bg=YELLOW)
checkmarks.grid(row=3,column=1)


window.mainloop()


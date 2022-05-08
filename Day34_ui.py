from tkinter import *

from Day34_quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score 0", pady=20, bg=THEME_COLOR ,fg="white", font=('Arial', 10, 'bold'))
        self.score_label.grid(row=0, column=1, sticky='new')
        # canvas / question
        self.canvas = Canvas(height=250, width=300,bg="white", highlightthickness=0)
        self.canvas.grid(pady=40,row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(150,125, width=280,text='Amazon acquired Twitch in August 2014 for $970 million dollars.', font=('Arial', 15, 'italic'))

        # buttons
        true_image = PhotoImage(height=97, width=100,file='Day34_images/true.png')
        false_image = PhotoImage(file='Day34_images/false.png')
        true_button = Button(image=true_image,bg=THEME_COLOR, bd=0, highlightthickness=0, command=lambda: self.button_pressed("true"))
        true_button.grid(row=2, column=0)
        false_button = Button(image=false_image,bg=THEME_COLOR, bd=0, highlightthickness=0, command=lambda: self.button_pressed("false"))
        false_button.grid(row=2, column=1)
        self.update_question() 
        self.window.mainloop()
        
        
    def button_pressed(self, s):
        print(f"{s} pressed")
        if self.quiz.check_answer(s):
            self.canvas.config(bg='#66ff66')
            self.update_score()
        else:
            self.canvas.config(bg='#ff4040')
        self.window.after(1000, lambda: self.reset_bg_and_next())
        
    def reset_bg_and_next(self):
        self.canvas.config(bg='white')
        self.update_question()
        
        
    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.get_score()}")
        
    def update_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
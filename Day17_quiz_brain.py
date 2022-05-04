class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def check_answer(self, my_ans, true_ans):
        if my_ans.lower() == true_ans.lower():
            print("You've got it right!")
            self.score += 1
        else:
            print("You've got it wrong!")
            print("Correct answer was: "+ true_ans)
    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {question.question}. (True/False)?: ")
        self.check_answer(ans, question.answer)
        if self.still_has_questions():
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print(f"Your final score is: {self.score}/{self.question_number}")
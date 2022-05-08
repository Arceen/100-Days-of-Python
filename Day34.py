from Day34_question_model import Question
from Day34_data import question_data
from Day34_quiz_brain import QuizBrain
from Day34_ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
while quiz.still_has_questions():
    print("here")
    quiz_ui.next_question(quiz.update_question())
    

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# Day 17 - Classes
from Day17_data import question_data
from Day17_question_model import Question
from Day17_quiz_brain import QuizBrain
# class User:
#     def __init__(self, id, username):
#         self.id = id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#         self.follower_list = []
#         self.following_list = []
#     def follow(self, user):
#         user.followers+=1
#         user.follower_list.append(self.username)
#         self.following+=1
#         self.following_list.append(user.username)
#     def __str__(self):
#         return f"{self.username} has {self.followers} followers, They are {self.follower_list}.\n{self.username} is following {self.following} people, They are {self.following_list}."
# user1 = User(1, "Abel")
# user2 = User(2, "Cain")
# user1.follow(user2)
# print(user1)
# print(user2)

question_bank = [Question(i['question'], i['correct_answer']) for i in question_data["results"]]
quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

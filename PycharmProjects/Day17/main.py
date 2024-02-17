# class User:
#     def __init__(self, my_id, username):
#         print("Hiiiiiiiii")
#         self.id = my_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user1 = User("10", "P")
# user2 = User("21", "D")
# user1.follow(user2)
#
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)

from question_model import Question
from data import question_data
from quiz_file import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_ques = Question(question_text, question_answer)
    question_bank.append(new_ques)

# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_questions():
    quiz.next_ques()

print("Quiz Completed")
print(f"your final score was {quiz.score_value}/{quiz.ques_no}")
# print(f"your final score was {quiz.score_value}/{len(question_bank)}")

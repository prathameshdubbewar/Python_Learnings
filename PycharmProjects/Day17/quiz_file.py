class QuizBrain:
    def __init__(self, ques_list):
        self.ques_no = 0
        self.score_value = 0
        self.ques_list = ques_list

    def still_questions(self):
        return self.ques_no < len(self.ques_list)
        # will return True / False

    def next_ques(self):
        current_ques = self.ques_list[self.ques_no]
        self.ques_no += 1
        user_reply = input(f"{self.ques_no}: {current_ques.text} (True/False): ")
        self.check_ans(user_reply, current_ques.answer)

    def check_ans(self, user_reply, correct_ans):
        if user_reply.lower() == correct_ans.lower():
            self.score_value += 1
            print("Correct Answer")
        else:
            print("That's Wrong")
        print(f"The correct Answer was : {correct_ans}.")
        print(f"your score is {self.score_value}/{self.ques_no}")
        print("\n")

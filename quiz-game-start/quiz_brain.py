class Quizbrain:
    score = 0

    def __init__(self, q_list):
        self.question_number=0
        self.question_list= q_list

    def still_ques(self):
         return self.question_number < len(self.question_list)#its right has last shd be pre known

    def next_question(self):
        current_ques= self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_ques.text} (True/False):")
        self.check_answer(user_answer, current_ques.answer)

    def check_answer(self, user_ans, crct_ans):
        if user_ans.lower()==crct_ans.lower():
            self.score += 1
            print("Your Right!!!!")
        else:
            print("Your Wrong :(")
        print("Correct answer:", crct_ans)
        print(f"Caution your score: {self.score}/{self.question_number}")




from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

ques_bank=[]
for keys in question_data:
    ques_text= keys["text"]
    ques_ans= keys["answer"]
    new_ques= Question(ques_text,ques_ans)
    ques_bank.append((new_ques))

quiz= Quizbrain(ques_bank)
while quiz.still_ques():
    quiz.next_question()
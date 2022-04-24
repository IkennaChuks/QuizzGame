from question_model import Question
from data import question_data
from  quiz_brain import Quizbrain

question_bank = []

for k in range(12):
    question_bank.append(Question(question_data[k]['text'],question_data[k]['answer']))


quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


else :
    final_score = quiz.score
    total_question = quiz.question_no
    print(f"You've completed the quiz \nYour final score was : {final_score} / {total_question}")
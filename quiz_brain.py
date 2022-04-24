class Quizbrain:

    def __init__(self,questions):
        self.question_no = 0
        self.questionlist = questions
        self.score = 0

    def still_has_questions(self):
        if len(self.questionlist) >= (self.question_no + 1):
            return True
        return False

    def next_question(self):
        user_answer= input(f'Q.{self.question_no+1}: {self.questionlist[self.question_no].text}'
                           f' true or false: ')
        correct_answer = self.questionlist[self.question_no].answer
        self.question_no += 1

        self.check_answer(user_answer,correct_answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}")
        print(f'your current score is {self.score} / {self.question_no}')
        print("\n")








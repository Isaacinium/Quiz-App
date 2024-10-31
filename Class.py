class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_questions(self):
        answer_from_user = int(input('2+2= '))
        self.check_answer_from_user(answer_from_user)

    def check_answer_from_user(self, answer_from_user):
        if answer_from_user ==  self.answer:
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {self.answer}")

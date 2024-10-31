class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
    
    def is_correct(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
    
    def add_question(self, question_text, correct_answer):
        question = Question(question_text, correct_answer)
        self.questions.append(question)
    
    def ask_questions(self):
        for question in self.questions:
            user_answer = input(f"{question.text} ")
            if question.is_correct(user_answer):
                print(f"Correct!")
                self.score += 1
                print(f'Your score is: {self.score}')
            else:
                print(f"Incorrect. The correct answer is: {question.answer}")
    
    def display_score(self):
        print(f"Your final score is: {self.score}/{len(self.questions)}")


quiz = Quiz()
quiz.add_question("What is the capital of Kenya?", "nairobi")
quiz.add_question("What is the largest ocean in the world?", "pacific")
quiz.add_question("Who invented the telephone?", "alexander graham bell")

quiz.ask_questions()
quiz.display_score()
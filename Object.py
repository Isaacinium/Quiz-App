from Class import Quiz
question = '2+2= '
answer = 4

quiz = Quiz(question,answer)
result = quiz.ask_questions()
result2 = quiz.ask_questions()
print(result)
print(result2)
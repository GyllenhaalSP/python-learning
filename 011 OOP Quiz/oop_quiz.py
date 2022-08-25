"""
OOP quiz game. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from objprint import op

question_bank = []

for question in question_data:
    text = question['question']
    answer = question['correct_answer']
    question_bank.append(Question(text, answer))

op(question_bank)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():

    quiz.next_question()

print('You\'ve completed the quiz')
print(f'Your final score was: {quiz.score}/{len(question_bank)}')

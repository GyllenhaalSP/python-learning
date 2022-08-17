"""
 By GyllenhaalSP jul. 2022 @ https://github.com/GyllenhaalSP.
"""
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
turtle.speed(0)
turtle.ht()

bet = turtle.textinput('Bet now!',
                       'Who will be the winner? Enter a color '
                       '(red, blue, green, gold, orange, brown): ').lower()

race = False
names = ['timmy', 'tammy', 'tommy', 'eenie', 'meenie', 'minie', 'moe']
colors = ['red', 'violet', 'blue', 'brown', 'gold', 'orange', 'green']
y_positions = [120, 80, 40, 0, -40, -80, -120]
all_turtles = []

for num in range(7):
    names[num] = Turtle('turtle')
    names[num].color(colors[num])
    names[num].penup()
    names[num].setpos(x=-230, y=y_positions[num])
    all_turtles.append(names[num])

while True:
    if bet in ('red', 'violet', 'blue', 'brown', 'gold', 'orange', 'green'):
        race = True
        break
    else:
        bet = turtle.textinput('Bet now!',
                               'Who will be the winner? Enter a color '
                               '(red, blue, green, gold, orange, brown): ').lower()

while race:
    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            race = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f'You\'ve won! The {winner} turtle is the winner!')
            else:
                print(f'You\'ve lost! The {winner} turtle is the winner!')
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()

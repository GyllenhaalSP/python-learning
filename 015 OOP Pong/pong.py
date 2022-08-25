"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard, Divider
from ball import Ball
from time import sleep

window = Screen()
window.setup(width=810, height=700)
window.bgcolor('black')
window.title('Pong')
window.tracer(0)
window.listen()

right_paddle = Paddle(370)
window.onkeypress(lambda key='up': right_paddle.move(key), 'Up')
window.onkeypress(lambda key='down': right_paddle.move(key), 'Down')

left_paddle = Paddle(-380)
window.onkeypress(lambda key='w': left_paddle.move(key), 'w')
window.onkeypress(lambda key='s': left_paddle.move(key), 's')

ball = Ball()
scoreboard = Scoreboard()

for height in range(4):
    Divider(ycor=100*height)
    Divider(ycor=-100*height)

while True:
    window.update()
    sleep(ball.sleep_timer)

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.bounce(x=True)

    if ball.distance(left_paddle) < 100 and ball.xcor() < -360:
        ball.bounce(x=True)

    if ball.xcor() > 385:
        scoreboard.score_up(score_left=1)
        ball.move(True)

    if ball.xcor() < -385:
        scoreboard.score_up(score_right=1)
        ball.move(True)
    window.update()
    ball.move()

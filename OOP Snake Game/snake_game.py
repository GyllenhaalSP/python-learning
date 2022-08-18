"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Screen
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard
from time import sleep

window = Screen()
window.setup(width=700, height=700)
window.bgcolor('black')
window.title('Snake Game')
window.tracer(0)

sir_hiss = Snake()
mouse = Food()
scoreboard = Scoreboard()

window.onkeypress(lambda key='up': sir_hiss.change_direction(key), "Up")
window.onkeypress(lambda key='down': sir_hiss.change_direction(key), "Down")
window.onkeypress(lambda key='left': sir_hiss.change_direction(key), "Left")
window.onkeypress(lambda key='right': sir_hiss.change_direction(key), "Right")
window.listen()

while True:
    window.update()
    sleep(0.1)

    sir_hiss.move()

    if sir_hiss.head.distance(mouse) < 25:
        mouse.reset_position()
        sir_hiss.add_body_part()
        scoreboard.score_up(1)

    if sir_hiss.head.xcor() < -350 or sir_hiss.head.xcor() > 350 or \
            sir_hiss.head.ycor() < -350 or sir_hiss.head.ycor() > 350:
        break

    if any(sir_hiss.head.distance(body_part) < 10 for body_part in sir_hiss.body[1:]):
        break

scoreboard.game_over()
window.exitonclick()

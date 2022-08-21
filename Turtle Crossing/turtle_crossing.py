"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

window = Screen()
window.setup(width=600, height=600)
window.tracer(0)

scoreboard = Scoreboard()
player = Player()

window.onkeypress(player.move_up, 'Up')
window.listen()

car_manager = CarManager()

while True:
    sleep(0.1)
    window.update()

    car_manager.car_making()
    car_manager.car_moving()

    if player.distance(0, 270) < 10:
        scoreboard.lvl_up()
        car_manager.speed_inc_on_lvl_up()
        player.goto(player.start)

    for car_obj in car_manager.garage:
        if car_obj.distance(player) < 20:
            break
    else:
        continue
    break

scoreboard.game_over()

window.exitonclick()

"""
 By GyllenhaalSP jul. 2022 @ https://github.com/GyllenhaalSP.
"""
import turtle as timmy
import random

tim = timmy.Turtle()
screen = timmy.Screen()

INITIAL_Y = -300
INITIAL_X = -300
INCREMENT_Y = 60

screen.setup(2200, 1350)
screen.title('Hirst Painting')
tim.shape("turtle")
tim.color("firebrick1")
tim.screen.colormode(255)
tim.speed(0)

rgb_colors = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50),
              (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
              (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
              (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
              (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]


line_counter = 0
tim.pu()
while line_counter <= 9:
    tim.setpos(INITIAL_X, INITIAL_Y + INCREMENT_Y)
    for line in range(10):
        tim.color(random.choice(rgb_colors))
        tim.dot(30)
        tim.pu()
        tim.fd(60)
    line_counter += 1
    INCREMENT_Y += 60

tim.ht()

screen.exitonclick()

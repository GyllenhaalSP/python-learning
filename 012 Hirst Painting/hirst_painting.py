"""
 By GyllenhaalSP jul. 2022 @ https://github.com/GyllenhaalSP.
"""
import turtle as timmy
import itertools
import random

INITIAL_X, INITIAL_Y = (-300, -300)
DOT_DISTANCE = 60
N_ROWS = 10
N_COLS = 10

tim = timmy.Turtle()
screen = timmy.Screen()
screen.setup(1024, 720)
screen.title('Hirst Painting')
tim.shape("turtle")
tim.color("firebrick1")
tim.screen.colormode(255)
tim.speed(0)

# RGB colors from colorama.
rgb_colors = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50),
              (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
              (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
              (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
              (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]


def pick_random_color():
    """
    Returns a random color from color list.
    """
    return random.choice(rgb_colors)


tim.pu()
for row, col in itertools.product(range(N_ROWS), range(N_COLS)):
    tim.setpos(INITIAL_X + col * DOT_DISTANCE, INITIAL_Y + row * DOT_DISTANCE)
    tim.dot(30, pick_random_color())

tim.ht()

screen.mainloop()

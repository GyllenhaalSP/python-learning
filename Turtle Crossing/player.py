"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    A class that represents the player. Inherits from turtle.
    """
    def __init__(self):
        super().__init__()
        self.start = STARTING_POSITION
        self.pu()
        self.st()
        self.shape('turtle')
        self.color('black')
        self.speed(0)
        self.seth(90)
        self.setpos(self.start)

    def move_up(self):
        """
        Moves player up by a fixed distance on the y-axis.
        """
        self.goto(0, self.ycor() + MOVE_DISTANCE)

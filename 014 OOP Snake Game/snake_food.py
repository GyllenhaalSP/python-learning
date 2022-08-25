"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Turtle
import random


class Food(Turtle):
    """
    A class that represents snake food, inheriting from Turtle.
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed(0)
        self.reset_position()

    def reset_position(self):
        """
        Sets the food's position randomly.
        """
        self.setpos(random.randint(-280, 280), random.randint(-280, 280))

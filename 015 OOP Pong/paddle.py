"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Turtle
MOVE_STEP = 40


class Paddle(Turtle):
    """
    A class that represents a Paddle, inheriting from Turtle.
    """

    def __init__(self, xcor, ycor=0):
        """
        Initializes paddle attributes.
        """
        super().__init__()
        self.color('white')
        self.shape('square')
        self.pu()
        self.setpos(xcor, ycor)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move(self, direction):
        """
        Changes paddle's direction.
        """
        match direction:
            case 'up' | 'w':
                self.setpos(self.xcor(), self.ycor() + MOVE_STEP)
            case 'down' | 's':
                self.setpos(self.xcor(), self.ycor() - MOVE_STEP)

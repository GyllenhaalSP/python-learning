"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Turtle
from random import choice, randint


class Ball(Turtle):
    """
    A class that represents a ball, inheriting from Turtle.
    """
    def __init__(self):
        """
        Initializes the ball attributes.
        """
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.setpos(0, 0)
        self.shapesize(stretch_wid=1.3, stretch_len=1.3)
        self.x_move = randint(25, 40)
        self.y_move = randint(25, 40)
        self.sleep_timer = 0.09

    def move(self, reset=False):
        """
        Moves the ball to a new position following a straight line. If flagged for reset, when the ball goes out of
        the boundaries, it resets the ball to the center of the screen and bounces it randomly in a random direction.
        """
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

        if reset:
            self.setpos(0, 0)
            self.x_move = randint(10, 25)
            self.y_move = randint(10, 25)
            match choice([1, 2, 3, 4]):
                case 1:
                    self.bounce(x=True)
                case 2:
                    self.bounce()
                case 3:
                    self.move()
                case 4:
                    self.bounce(x=True)
                    self.bounce()

            self.sleep_timer = 0.09

    def bounce(self, x=None):
        """
        Bounces the ball in the -x-axis when the x argument is passed, else it bounces to the -y-axis.
        """
        self.sleep_timer *= 0.9
        if x:
            self.x_move *= -1
        else:
            self.y_move *= -1

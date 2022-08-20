"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Turtle
ALIGN = 'center'
FONT = ('Fixedsys', 50, 'bold')


class Scoreboard(Turtle):
    """
    A class that represents a Scoreboard, inheriting from Turtle.
    """
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color('white')
        self.speed(0)
        self.right_player_score = 0
        self.left_player_score = 0
        self.refresh()

    def refresh(self):
        """
        Refresh the scoreboard.
        """
        self.clear()
        self.goto(-200, 270)
        self.write(f'{self.left_player_score}', align=ALIGN, font=FONT)
        self.goto(200, 270)
        self.write(f'{self.right_player_score}', align=ALIGN, font=FONT)

    def score_up(self, score_right=0, score_left=0):
        """
        Increments the correct side of the scoreboard.
        """
        self.right_player_score += score_right
        self.left_player_score += score_left
        self.refresh()


class Divider(Turtle):
    """
    A class that represents the field divider, inheriting from Turtle.
    """
    def __init__(self, ycor=0):
        """
        Initializes the divider attributes.
        """
        super().__init__()
        self.color('white')
        self.shape('square')
        self.pu()
        self.setpos(0, ycor)
        self.shapesize(stretch_wid=2.5, stretch_len=0.3)

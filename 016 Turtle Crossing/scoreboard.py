"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Turtle
ALIGN = ('left', 'center', 'right')
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    """
    A class that represents a Scoreboard, inheriting from Turtle.
    """
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color('black')
        self.speed(0)
        self.lvl = 0
        self.refresh()

    def refresh(self):
        """
        Refresh the scoreboard.
        """
        self.clear()
        self.goto(-150, 250)
        self.write(f'Level: {self.lvl}', align=ALIGN[2], font=FONT)

    def lvl_up(self):
        """
        Increments the level counter whenever the conditions are met.
        """
        self.lvl += 1
        self.refresh()

    def game_over(self):
        """
        Signals the game over.
        """
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGN[1], font=FONT)

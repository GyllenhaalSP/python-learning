"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Turtle
ALIGN = 'center'
FONT = ('Fixedsys', 25, 'bold')


class Scoreboard(Turtle):
    """"
    A class that represents a Scoreboard, inheriting from Turtle.
    """
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color('grey')
        self.speed(0)
        self.setpos(0, 300)
        self.score = 0
        self.refresh_score(False)

    def refresh_score(self, game_status):
        """
        Refresh the scoreboard and routes the game over.
        """
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)
        if game_status:
            self.setpos(0, 0)
            self.write('GAME OVER', align=ALIGN, font=FONT)

    def score_up(self, score):
        """
        Increments the scoreboard by score.
        """
        self.score += score
        self.refresh_score(False)

    def game_over(self):
        """
        Sends the signal to write game over.
        """
        self.refresh_score(True)

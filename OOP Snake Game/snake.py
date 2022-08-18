"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Turtle

MOVE_STEP = 20
STARTING_BODY_DISPLACEMENT = (-20 * body_part for body_part in range(3))
STARTING_POS = [(X_POS, 0) for X_POS in STARTING_BODY_DISPLACEMENT]
DIRECTIONS = {'right': 0, 'up': 90, 'left': 180, 'down': 270}


class Snake:
    """
    Represents the head and the body and body parts of the snake.
    """

    def __init__(self):
        """
        Initializing the snake's head and body.
        """
        self.body = []
        self.create()
        self.head = self.body[0]

    def create(self):
        """
        Creates the starting body parts of the snake.
        """
        for coord in STARTING_POS:
            self.grow_body_part(coord)

    def move(self):
        """
        Moves the snake forward continuously, making each subsequent piece follow the head.
        """
        for body_part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[body_part - 1].xcor()
            new_y = self.body[body_part - 1].ycor()
            self.body[body_part].goto(new_x, new_y)
        self.head.forward(MOVE_STEP)

    def grow_body_part(self, coord):
        """
        Grows a new piece of the snake body.
        """
        body_part = Turtle('square')
        body_part.color('white')
        body_part.pu()
        body_part.setpos(coord)
        self.body.append(body_part)

    def add_body_part(self):
        """
        Attaches a body part to the end of the snake body.
        """
        self.grow_body_part(self.body[-1].position())

    def change_direction(self, direction):
        """
        Changes snake's direction.
        """
        match direction:
            case 'up':
                if self.head.heading() != DIRECTIONS['down']:
                    self.head.seth(DIRECTIONS['up'])
            case 'down':
                if self.head.heading() != DIRECTIONS['up']:
                    self.head.seth(DIRECTIONS['down'])
            case 'left':
                if self.head.heading() != DIRECTIONS['right']:
                    self.head.seth(DIRECTIONS['left'])
            case 'right':
                if self.head.heading() != DIRECTIONS['left']:
                    self.head.seth(DIRECTIONS['right'])

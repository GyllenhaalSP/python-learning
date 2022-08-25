"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from turtle import Turtle
from random import choice, randrange
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """
    A class that represent a car manager. Inherits from turtle.
    """
    def __init__(self):
        super().__init__()
        self.garage = []
        self.ht()
        self.speed = STARTING_MOVE_DISTANCE

    def car_making(self):
        """
        Makes a new random car.
        """
        match randrange(1, 6):
            case 5:
                car = Turtle('square')
                car.st()
                car.pu()
                car.color(choice(COLORS))
                car.speed(0)
                car.shapesize(stretch_wid=1, stretch_len=2)
                car.setpos(300, randrange(-220, 250))
                self.garage.append(car)

    def car_moving(self):
        """
        Moves a car.
        """
        for car in self.garage:
            car.backward(self.speed)

    def speed_inc_on_lvl_up(self):
        """
        Increases car speed every new level.
        """
        self.speed += MOVE_INCREMENT

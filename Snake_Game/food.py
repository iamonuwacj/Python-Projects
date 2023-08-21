import random
from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh()

    def refresh(self):
        random_x = randint(-260, 260)
        random_y = randint(-260, 260)
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.penup()
        self.goto(random_x, random_y)

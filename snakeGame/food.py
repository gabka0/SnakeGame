from turtle import Turtle, Screen
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        xRandom = randint(-280,280)
        yRandom = randint(-280,265)
        self.goto(xRandom, yRandom)

    def refresh(self):
        xRandom = randint(-280, 280)
        yRandom = randint(-280, 280)
        self.goto(xRandom, yRandom)



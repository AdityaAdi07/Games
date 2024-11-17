from turtle import Turtle
import random


class Food(Turtle): # inherithing Turtle class like blud.shape becomes self.shape as Food= Turtle

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  #  normally it is 20x20 but we want smaller 10x10
        self.color('white')
        self.speed('fastest')  #  to skip food spwan animation
        self.refresh()

    def refresh(self):
        y_nxt= random.randint(-285,285)
        if y_nxt!= 275:
            self.goto(x=random.randint(-285, 285), y=y_nxt)
        else:
            pass

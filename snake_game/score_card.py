from turtle import Turtle


class ScoreCard(Turtle):
    def __init__(self):
        self.a = 0  #  use seld so that it can be carried to next method also
        with open("data") as file:
            self.high=int(file.read())
        super().__init__()
        self.hideturtle()
        self.setpos(0,275)
        self.color("yellow")
        self.penup()
        self.write(f'SCORE CARD: {self.a}    |    HIGH-SCORE: {self.high}', False, 'center', ('arial', 15, 'bold'))

    def update(self):
        self.clear()
        self.write(f'SCORE CARD: {self.a}    |    HIGH-SCORE: {self.high}', False, 'center', ('arial', 15, 'bold'))
    def reset(self):
        if self.a>self.high:   #  to update high score
            self.high= self.a
            with open("data", mode='w') as file:
                file.write(f'{self.high}')

        self.a=0
        self.update()

    def count(self):
        self.a+=1
        self.update()



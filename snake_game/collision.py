from turtle import Turtle

class Collision(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.hideturtle()

    def stop(self):
        self.write('GAME OVER !!!',False, 'Center', ('arial',15,'bold') )

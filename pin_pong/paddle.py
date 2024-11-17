from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,postion):  #  pos bcz we need left to go to -350 n right to go 350
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1) #  we get 20x5=100 and 20 rectangle
        self.goto(postion)

    def move_up(self):
        new_y= self.ycor() + 20    #  we cant do a iteration method as we need 2 x and y coord
        # can only do by self xcor and ycor coz self knws smtng
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



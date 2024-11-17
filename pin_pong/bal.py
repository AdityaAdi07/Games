from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.x_move= 10  #  we created a new var so can be manipulated
        self.y_move= 10
        self.pace=0.1 #  setting attribute
    def move(self):
        new_x= self.xcor()+ self.x_move
        new_y= self.ycor()+ self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1 #  here to bounce remember reflection so only the y cor rev x is same movement

    def bounce_x(self):
        self.x_move *= -1
        self.pace *=0.9  #  never use increment option coz it lags the code


    def restart(self):
        self.goto(0,0)  #  go to home is engh here thn it will carry the move function
        self.pace=0.1
        self.bounce_x()  #  bounce_x will allow the ball to go to left side if right paddle misses
                         #  its actually like telling x_move to increment by -1 every time
                         # if we assign nex_x or x_move to -1 then it will go down rather left side

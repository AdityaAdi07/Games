from turtle import Turtle

class Print(Turtle):
    def __init__(self):
        self.a=0
        self.b=0
        super().__init__()
        self.hideturtle()
        self.setpos(0, 260)
        self.color("yellow")
        self.penup()
        self.write(f'{self.b}     :     {self.a}', False, 'center', ('arial', 20, 'bold'))


    def KO(self):
        self.color('Yellow')
        self.penup()
        self.hideturtle()
        self.write('GAME OVER!!!', False, 'center', ('arial', 20, 'bold'))

    def score_1(self):
        self.a +=1
        self.clear()
        self.write(f'{self.b}     :      {self.a}', False, 'center', ('arial', 20, 'bold'))

    def score_2(self):
        self.b += 1
        self.clear()
        self.write(f'{self.b}     :     {self.a}', False, 'center', ('arial', 20, 'bold'))

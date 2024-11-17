from turtle import Turtle, Screen
import time
screen= Screen()

class Snake:

    def __init__(self):
        self.snke_parts=[]
        self.create_snake()

    def create_snake(self):
        self.a=0
        for turtle in range(0, 3):
            blud = Turtle()
            blud.shape('square')
            blud.color('white')
            blud.penup()
            blud.setpos(x=0 - self.a, y=0)
            self.a += 20
            self.snke_parts.append(blud)  #as we are operating with class we use self.segment

    def add_seg(self, position): # adds new segment same as bfr so copy, and return postion so we req nxt meth
        blud = Turtle()
        blud.speed('fastest')
        blud.shape('square')
        blud.color('white')
        blud.penup()
        blud.setpos(self.snke_parts[-1].position())  #  new part is added at end of the snake list and keeping this
        #  pos here will also help in not getting that spawning of block at begining
        self.snke_parts.append(blud)

    def extend(self):
        self.add_seg(self.snke_parts[-1].position())


    def move_snake(self):

        for seg_prt in range(len(self.snke_parts) - 1, 0, -1):  # here its 3 to 1 in rev order so -1 as step
            nxt_x = self.snke_parts[seg_prt - 1].xcor()
            nxt_y = self.snke_parts[seg_prt - 1].ycor()
            self.snke_parts[seg_prt].goto(nxt_x, nxt_y)
        self.snke_parts[0].fd(10) #this is must as snake shd be always moving

    def move_up(self):
        if self.snke_parts[0].heading()==270: #here chaning 0 is engh as we did thr abv part
            pass
        else:
            self.snke_parts[0].setheading(90)
    def move_down(self):
        if self.snke_parts[0].heading()==90: #always specify the blud in list
            pass
        else:
            self.snke_parts[0].setheading(270)

    def move_right(self):
        if self.snke_parts[0].heading() == 180:
            pass
        else:
            self.snke_parts[0].setheading(0)
    def move_left(self):
        if self.snke_parts[0].heading() == 0:
            pass
        else:
            self.snke_parts[0].setheading(180)


    def restart(self):
        for seg in self.snke_parts:
            seg.goto(900,900)
        self.snke_parts.clear()
        self.create_snake()








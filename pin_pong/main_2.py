from turtle import Screen
from paddle import Paddle
from bal import Ball
from prints import Print
import time

is_game_on= True
screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)
pong= Ball()
printss= Print()
bar_1= Paddle((370,0))
bar_2= Paddle((-370,0)) # now we can put as we have that arguement


screen.listen()
screen.onkey(bar_1.move_up,'Up')
screen.onkey(bar_1.move_down,'Down')
screen.onkey(bar_2.move_up,'w')
screen.onkey(bar_2.move_down,'s')

while is_game_on:
    time.sleep(pong.pace)  #  to slow down the moment of ball so we can vizualize
    screen.update()
    pong.move()

    if pong.ycor()> 285 or pong.ycor()<-285:
        pong.bounce_y()
    if pong.xcor() > 350 and pong.distance(bar_1)< 50 or pong.xcor()< -350 and pong.distance(bar_2)< 50:
        pong.bounce_x()


    elif pong.xcor()>380:
        printss.score_2()
        pong.restart()
    elif pong.xcor()<-380:
        printss.score_1()
        pong.restart()




screen.exitonclick()
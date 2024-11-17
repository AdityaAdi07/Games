from turtle import Screen
from snake import Snake
from food import Food
from score_card import ScoreCard
from collision import Collision
import time

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0) # turns off the animation

snake= Snake()
food= Food()
score= ScoreCard()
collide= Collision()

screen.listen()
screen.onkey(snake.move_up,'w')  # dont put () after snake.move coz it takes no input
screen.onkey(snake.move_down,'s')
screen.onkey(snake.move_left,'a')
screen.onkey(snake.move_right,'d')

is_game_on= True
while is_game_on:
    screen.update()  # by placing update here it will show int location and updates after all the segments move and not one by one
    # used to undo tracer operation has that makes the animation invis
    time.sleep(0.1)  # instead of delay after each 3 it has delay after all 3
    snake.move_snake()

    if snake.snke_parts[0].distance(food) < 14: #from snake part call head snake part
        food.refresh()  #  here from food class we are calling refresh method
        score.count()
        snake.extend()
    if snake.snke_parts[0].xcor()>285 or snake.snke_parts[0].xcor()<-290 or snake.snke_parts[0].ycor()<-287 or snake.snke_parts[0].ycor()>290:
        score.reset()
        snake.restart()


    for ech_part in snake.snke_parts[1:]: #  we took from pos 1 to all, not frm 0
        if snake.snke_parts[0].distance(ech_part) < 10:
            score.reset()
            snake.restart()

screen.exitonclick()






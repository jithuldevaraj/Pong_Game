from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


# Create Object
screen = Screen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()


# Screen setup
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()































screen.exitonclick()

from turtle import Screen
from paddle import Paddle


# Create Object
screen = Screen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


# Screen setup
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")































screen.exitonclick()

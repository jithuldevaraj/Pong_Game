from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("circle")
        self.color("white")

    def move(self):
        new_x = self.xcor() + 2
        new_y = self.ycor() + 5
        self.goto(new_x, new_y)
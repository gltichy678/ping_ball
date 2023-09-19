from turtle import Turtle


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def move_ball(self):
        new_x_move = self.x_move + self.xcor()
        new_y_move = self.y_move + self.ycor()
        self.goto(new_x_move, new_y_move)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.y_move *= 1
        self.x_move *= -1

    def bounce_y(self):
        self.x_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)

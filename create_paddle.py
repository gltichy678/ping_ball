from turtle import Turtle, Screen

screen = Screen()


class create_paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos_x, pos_y)

    def right_move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def right_move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def left_move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def left_move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

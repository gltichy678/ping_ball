from turtle import Turtle, Screen


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.l_score = 0
        self.r_score = 0
        self.goto(-200, 250)
        self.write(self.l_score, align="center", font=("Verdana", 30, "normal"))
        self.goto(200, 250)
        self.write(self.r_score, align="center", font=("Verdana", 30, "normal"))

    def update_score(self, pad):
        if pad == 'r':
            self.r_score += 1
            self.clear()
            self.goto(200, 250)
            self.write(self.r_score, align="center", font=("Verdana", 30, "normal"))
            self.goto(-200, 250)
            self.write(self.l_score, align="center", font=("Verdana", 30, "normal"))
        elif pad == 'l':
            self.l_score += 1
            self.clear()
            self.goto(-200, 250)
            self.write(self.l_score, align="center", font=("Verdana", 30, "normal"))
            self.goto(200, 250)
            self.write(self.r_score, align="center", font=("Verdana", 30, "normal"))

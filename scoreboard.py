from turtle import Turtle
FONT = "Droid", 40, "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_scoreboard()

    def dividers(self):
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=1.5)
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.setheading(270)
        for underscore in range(10):
            self.stamp()
            self.forward(60)

    def update_scoreboard(self):
        self.clear()
        self.dividers()
        self.goto(-20, 220)
        self.write(f"{self.score_l}", align="right", font=FONT)
        self.goto(20, 220)
        self.write(f"{self.score_r}", align="left", font=FONT)

    def point_l(self):
        self.score_l += 1
        self.update_scoreboard()

    def point_r(self):
        self.score_r += 1
        self.update_scoreboard()

    def game_over(self, winner):
        self.goto(100, -30)
        self.write(f"{winner} player wins", align="right", font=FONT)

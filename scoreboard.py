from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.score = 0

    def level_up(self):
        self.score += 1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.goto(0, 220)
        self.write(f"Level: {self.score}", align="center", font=FONT)
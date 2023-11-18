import time
from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.goto(x=-200, y=250)
        self.write(f"Level : {self.level}", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
        self.level = 1

    def cleear(self):
        self.clear()
        self.update_score()
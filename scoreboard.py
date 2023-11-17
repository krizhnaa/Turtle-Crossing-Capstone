from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(x=-200, y=250)
        self.update_score()

    def update_score(self):
        self.write(f"Level : {self.level}", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_score()

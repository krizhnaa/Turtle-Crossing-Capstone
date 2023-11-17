from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
y_distance = random.sample(range(-250, 250 + 1), 1)
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(280, y_distance[0])
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)

    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE)



from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
y_distance = random.sample(range(-250, 250 + 1), 100)


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        n_car = Turtle()
        n_car.shape('square')
        n_car.shapesize(stretch_wid=1, stretch_len=2)
        n_car.penup()
        n_car.color(random.choice(COLORS))
        n_car.goto(280, random.choice(y_distance))
        self.cars.append(n_car)

    def car_move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)



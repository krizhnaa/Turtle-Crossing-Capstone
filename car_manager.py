import time
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0
y_distance = random.sample(range(-200, 225 + 1), 100)


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        rand_int = random.randint(0, 10)
        if rand_int == 3 or rand_int == 4:
            n_car = Turtle()
            n_car.shape('square')
            n_car.shapesize(stretch_wid=1, stretch_len=2)
            n_car.penup()
            n_car.color(random.choice(COLORS))
            n_car.goto(280, random.choice(y_distance))
            self.cars.append(n_car)

    def car_move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + self.car_speed)

    def restart(self):
        for car in self.cars:
            car.goto(380, 380)
        self.cars = []
        self.car_speed = 0

    def level_up(self):
        self.car_speed += 10
        self.car_move()






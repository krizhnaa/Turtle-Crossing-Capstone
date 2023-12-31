import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)
car = CarManager()
score = Scoreboard()
player = Player()
screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, 'Up')
    car.create_car()
    car.car_move()

    if player.ycor() > 280:
        print("Finished")
        score.level_up()
        player.next_level()
        car.level_up()

    for kar in car.cars:
        if kar.distance(player) < 27:
            print('Collision')
            player.starting_pos()
            car.restart()
            score.game_over()
            game_is_on = False


screen.exitonclick()



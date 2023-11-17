import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

score = Scoreboard()
player = Player()
screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, 'Up')
    if player.ycor() > 280:
        print("Finished")
        score.level_up()
        player.next_level()

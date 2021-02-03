import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

playboy = Player()
carz = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(playboy.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carz.create_car()
    carz.move_cars()

    for car in carz.all_cars:
        if car.distance(playboy) < 20:
            game_is_on = False
            score.game_over()

    if playboy.is_at_finish_line():
        playboy.go_to_start()
        carz.level_up()
        score.increase_level()

screen.exitonclick()
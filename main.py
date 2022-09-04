"""
frogger
"""
# import classes and modules
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Frogger")

# create game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# set up listener
screen.listen()
screen.onkey(player.go_up, "Up")


GAME_IS_ON = True

while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect player collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            GAME_IS_ON = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        scoreboard.level_up()
        player.reset_position()
        car_manager.level_up()


screen.exitonclick()

"""
car class - generate and move cars
"""
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """
    create car class
    """

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        create car object
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            self.hideturtle()
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(0)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        move cars
        """
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """
        increase speed of cars by 10 each
        time player levels up
        """
        self.car_speed += MOVE_INCREMENT

"""
player class - the turtle that the player will use to play game
"""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    create player object
    """

    def __init__(self):
        """
        create the turtle
        """
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.reset_position()
        self.setheading(90)

    def go_up(self):
        """
        move the turtle
        """
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        """
        returns True is player reaches finish line
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_position(self):
        """
        reset turtle to starting position
        """
        self.goto(STARTING_POSITION)

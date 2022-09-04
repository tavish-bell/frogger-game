"""
create and update game scoreboard
"""
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    create scoreboard object
    """

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        update scoreboard when player levels up
        """
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=(FONT))

    def level_up(self):
        """
        increase level on scoreboard
        """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """
        print game over message
        """
        self.goto(0, 0)
        self.write("Game over", align="center", font=(FONT))

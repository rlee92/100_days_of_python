from turtle import Turtle

ALIGNMENT= "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

    def game_over(self):
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

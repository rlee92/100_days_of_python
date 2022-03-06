from turtle import Turtle

ALIGNMENT= "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.goto(-200, 250)
        self.write(f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def level_up(self):
        self.current_level += 1
        self.clear()
        self.write(f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

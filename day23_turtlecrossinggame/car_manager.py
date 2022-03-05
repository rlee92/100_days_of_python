from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = STARTING_MOVE_DISTANCE
        for color_index in range(0,6):
            self.color(COLORS[color_index])

    def create_cars(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, 0)

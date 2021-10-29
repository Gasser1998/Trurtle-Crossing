from turtle import Turtle
import random


import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []


    def create_car(self):
            chance = random.randint(1,6)
            if chance == 1:
                car = Turtle("square")
                car.setheading(180)
                car.color(random.choice(COLORS))
                car.pu()
                car.shapesize(stretch_len=2,stretch_wid=1)
                x = 300
                y = random.randrange(-160,160)
                car.goto(x,y)
                self.cars.append(car)

    def move_car(self,speed):
        for x in range(0,len(self.cars)):
            self.cars[x].forward(speed)








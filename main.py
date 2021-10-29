import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=400)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard
player.turt()
player.outline()

screen.listen()



game_is_on = True

car_speed = 5
level = 1
hlevel = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if level > hlevel:
        hlevel = level
    # Checks if turtle has crossed the road
    if player.position() > 180:
        car_speed += 3.5
        level += 1

    score.scores(level,hlevel) #checks score and updates
    car.move_car(car_speed) #updates speed if player moves on to next level
    car.create_car() #creates new cars

    #Checks if turtle has collided with any cars
    for L in car.cars:
        if L.distance(player.hobbs.position()) < 20:
            print("Game Over")
            game_is_on = False
    #returns player back to original spot after crossing
    player.restart()
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")

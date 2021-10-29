from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player():

    def __init__(self):
        self.hobbs = Turtle("turtle")



    def turt(self):
        self.hobbs.pu()
        self.hobbs.goto(0, -190)
        self.hobbs.setheading(90)


# Used for moving turtle
    def up(self):
        self.hobbs.forward(10)

    def down(self):
        self.hobbs.backward(10)

# Used for game outline
    def outline(self):
        outline = Turtle()
        outline.pu()
        outline.goto(300, -170)
        outline.pd()
        outline.goto(-300,-170)
        outline.pu()
        outline.goto(-300, 170)
        outline.pd()
        outline.goto(300, 170)
        outline.hideturtle()

# restarts turtle back to original position
    def restart(self):
        if self.hobbs.ycor() > 180:
            self.hobbs.goto(0,-185)

# checks turtles position
    def position(self):
        return self.hobbs.ycor()








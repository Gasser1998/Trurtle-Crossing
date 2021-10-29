import turtle

FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard:

    def scores(plevel,hlevel):
        score = Turtle()
        score.pu()
        score.hideturtle()
        score.goto(-280,180)
        score.write(F"Level:{plevel}. Highscore:{hlevel}")
        score.clear()








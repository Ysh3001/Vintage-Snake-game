import fileinput
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 15, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = data.read()
            self.hs = int(self.high_score)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 275)
        self.update()

    def game_reset(self):
        if self.score > self.hs:
            self.hs = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.hs}")
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:"
                   f"{self.score} High Score:{self.hs}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update()





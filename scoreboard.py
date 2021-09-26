
from turtle import Turtle

FONT_STYLE = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as high:
            self.high_score = int(high.read())
        self.hideturtle()
        self.goto(0, 265)
        self.color("#D9CAB3")
        self.score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}, high score: {self.high_score}", align='center', font=FONT_STYLE)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align='center', font=("Courier", 24, "italic"))
        if self.score > self.high_score:
            with open("high_score.txt",mode="w") as high:
                high.write(f"{self.score}")

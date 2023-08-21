from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as f:
            self.high_score = int(f.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(font=FONT, align="center", arg=f"Score: {self.score}  High Score: {self.high_score}")

    def increase(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(f"{self.high_score}")
            self.goto(0, 0)
            self.write(arg=f"Game Over. New High Score: {self.high_score}", font=FONT, align="center")
        self.score = 0


from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto((0, 260))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center",
                   font=("Courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.score > self.high_score:
            self.high_score = self.score
        self.write("Game over.", move=False, align="center",
                   font=("Courier", 24, "bold"))

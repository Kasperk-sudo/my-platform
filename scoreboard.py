from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)



    def update_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

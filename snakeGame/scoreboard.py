from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.highest_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}. Highest Score: {self.highest_score}", align='CENTER', font=('Courier', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()
    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #   self.goto(0,0)
    #   self.write(f"Game Over", align='CENTER', font=('Courier', 15, 'normal'))






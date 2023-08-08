from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("spring green")
        self.goto(0, 270)
        self.player_1_score = 0
        self.player_2_score = 0
        self.write(f"{self.player_1_score} : {self.player_2_score}",
                   align='center', font=('Arial', 18, 'normal'))

    def update_player_1_score(self):
        self.player_1_score += 1
        self.update_scoreboard()
        print("yupp")

    def update_player_2_score(self):
        self.player_2_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # self.write(f"Player 1: 1 Player 2: 000",
        #            align='center', font=('Arial', 14, 'normal'))
        self.write(f"{self.player_1_score} : {self.player_2_score}",
                   align='center', font=('Arial', 18, 'normal'))

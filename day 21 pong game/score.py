from turtle import Turtle

FONT = ("Arial", 40, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score_left = 0
        self.score_right = 0
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.score_left}", True, "center", FONT)
      
        self.goto(100, 200)
        self.write(f"{self.score_right}", True, "center", FONT)

    def update_left_score(self): 
        self.score_left += 1

    def update_right_score(self): 
        self.score_right += 1

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER",True,"center",FONT)



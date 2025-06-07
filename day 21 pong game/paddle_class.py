from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.color("white")
        self.x = xcor
        self.y = ycor
        self.goto(self.x,self.y)
        
    def up(self):
        ycor = self.ycor() +20
        self.goto(self.x,ycor)
        
        
    
    def down(self):
        ycor = self.ycor() -20
        self.goto(self.x,ycor)
    
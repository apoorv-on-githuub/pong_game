from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  
        self.color("white")
        self.penup()
        self.X_SPEED = 10
        self.Y_SPEED = 10
        self.move() 
        self.ball_speed = 0.1

    def move(self):
        if self.collision_y()  == True:
            self.Y_SPEED = -1 * self.Y_SPEED
        x_cor = self.xcor() + self.X_SPEED
        y_cor = self.ycor() +  self.Y_SPEED
        self.goto(x=x_cor,y=y_cor)
        if abs(self.xcor()) < 300:  # away from paddle zones
            self.recently_bounced = False
 
    def collision_y(self):
        ycor = self.ycor()
        return ( ycor > 280 or ycor < -280)
    
    
    def collison_x(self):
        if not self.recently_bounced:
            self.X_SPEED *= -1
            self.ball_speed *= 0.7
            self.recently_bounced = True

    def ball_reset(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.collison_x()

   

            
        
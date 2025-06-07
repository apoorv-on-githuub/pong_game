from turtle import Screen
import time
from paddle_class import Paddle
from ball_class import Ball
from score import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

right_paddle =Paddle(350,0)
left_paddle = Paddle(-350,0)
ball = Ball()
score = Score()
maximum_score = screen.numinput("maimum score","maximum no of score (1 to 10)",5,1,10)

  

screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() >320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320 :
        ball.collison_x()

    if ball.xcor() > 373:
        ball.ball_reset()
        score.update_left_score()
    if ball.xcor() < -373:
        ball.ball_reset()  
        score.update_right_score()
    score.update_score()
    
    if score.score_left == maximum_score or score.score_left == maximum_score:
        game_is_on = False
        score.game_over()
        
screen.exitonclick()from turtle import Screen
import time
from paddle_class import Paddle
from ball_class import Ball
from score import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

right_paddle =Paddle(350,0)
left_paddle = Paddle(-350,0)
ball = Ball()
score = Score()
maximum_score = screen.numinput("maimum score","maximum no of score (1 to 10)",5,1,10)

  

screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() >320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320 :
        ball.collison_x()

    if ball.xcor() > 373:
        ball.ball_reset()
        score.update_left_score()
    if ball.xcor() < -373:
        ball.ball_reset()  
        score.update_right_score()
    score.update_score()
    
    if score.score_left == maximum_score or score.score_left == maximum_score:
        game_is_on = False
        score.game_over()
        
screen.exitonclick()from turtle import Screen
import time
from paddle_class import Paddle
from ball_class import Ball
from score import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

right_paddle =Paddle(350,0)
left_paddle = Paddle(-350,0)
ball = Ball()
score = Score()
maximum_score = screen.numinput("maimum score","maximum no of score (1 to 10)",5,1,10)

  

screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() >320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320 :
        ball.collison_x()

    if ball.xcor() > 373:
        ball.ball_reset()
        score.update_left_score()
    if ball.xcor() < -373:
        ball.ball_reset()  
        score.update_right_score()
    score.update_score()
    
    if score.score_left == maximum_score or score.score_left == maximum_score:
        game_is_on = False
        score.game_over()
        
screen.exitonclick()

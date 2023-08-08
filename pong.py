
from turtle import Turtle,Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle_1 = Paddle((-350,0))
paddle_2 = Paddle((350,0))

ball = Ball()

screen.listen()

screen.onkey(fun=paddle_2.up,key="Up")
screen.onkey(fun=paddle_2.down,key="Down")

screen.onkey(fun=paddle_1.up,key="w")
screen.onkey(fun=paddle_1.down,key="s")

scoreboard = Scoreboard()
dir = 1

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    # time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball.move()
        # dir = -1
        ball.bounce_y()

    # if ball.xcor() < -280:
    #     # ball.move()
    #     # dir = 1
    #     ball.bounce()

    if ball.distance(paddle_2) < 60 and ball.xcor() > 330:
        
        ball.bounce_x()
    if ball.distance(paddle_1) < 60 and ball.xcor() < -330:
        ball.bounce_x()
    if ball.xcor() > 400:
        # ball.goto(0,0)
        # ball.move()
        scoreboard.update_player_1_score()
        ball.reset_match()
    if ball.xcor()<-400:
        scoreboard.update_player_2_score()
        # ball.goto(0,0)
        # ball.move()
        ball.reset_match()









screen.exitonclick()

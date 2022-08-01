from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")

winning_score = 5
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.point_l()

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.point_r()

    if scoreboard.score_l == winning_score:
        game_is_on = False
        scoreboard.game_over("Left")
    elif scoreboard.score_r == winning_score:
        game_is_on = False
        scoreboard.game_over("Right")

screen.exitonclick()

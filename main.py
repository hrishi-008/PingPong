import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=800)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(l_paddle.go_up, 'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.resetpos()

    if ball.xcor() < -380:
        ball.resetpos()

screen.exitonclick()

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("#000000")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Check for a collision with the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check for a collision with the paddles
    if (
        ball.xcor() > 320
        and ball.distance(r_paddle) < 50
        or ball.xcor() < -320
        and ball.distance(l_paddle) < 50
    ):
        ball.bounce_x()

    # Check for a collision with the left or right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_score("left")

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_score("right")


screen.exitonclick()

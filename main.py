from turtle import Turtle, Screen
from create_paddle import create_paddle
from ball import ball
from scoreboard import scoreboard
import time

turtle = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping pong")
screen.tracer(0)
right_paddle = create_paddle(350, 0)
left_paddle = create_paddle(-350, 0)
pong = ball()
score = scoreboard()
screen.update()
screen.listen()
screen.onkey(key="w", fun=right_paddle.right_move_up)
screen.onkey(key="s", fun=right_paddle.right_move_down)
screen.onkey(key="a", fun=left_paddle.left_move_up)
screen.onkey(key="d", fun=left_paddle.left_move_down)
is_game_on = True
while is_game_on:
    i = 0
    time.sleep(pong.speed)
    screen.update()
    pong.move_ball()
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce()
    if (pong.distance(right_paddle) < 20 or (pong.xcor() > 340 and pong.distance(right_paddle) < 50)) or (
            pong.distance(left_paddle) < 20 or (pong.xcor() < -340 and pong.distance(left_paddle) < 50)):
        pong.paddle_bounce()
        pong.speed -= 0.005
    # right_paddle misses
    if pong.xcor() > 380:
        score.update_score('l')
        pong.speed = 0.1
        pong.reset_position()
        pong.bounce_y()
    # left paddle misses
    if pong.xcor() < -380:
        score.update_score('r')
        pong.speed = 0.1
        pong.reset_position()
        pong.bounce_x()

    if i == 3:
        if score.l_score > score.r_score:
            print(f"The left paddle is the winner")
            is_game_on = False
        elif score.r_score > score.l_score:
            print(f"The right paddle is he winner")
            is_game_on = False
    i += 1
screen.exitonclick()

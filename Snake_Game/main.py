from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    time.sleep(0.07)
    screen.update()

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase()
        scoreboard.increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        game_on = False
        print("game Over")

    for segments in snake.segments:
        if 0 < snake.head.distance(segments) < 9:
            scoreboard.reset()
            game_on = False
            print(snake.head.distance(segments))


screen.exitonclick()

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.snake_list[0].xcor() > 285 or snake.snake_list[0].xcor() < -285 or snake.snake_list[0].ycor() < -285 or snake.snake_list[0].ycor() > 285:
        snake.reset_snake()
        score.game_reset()

    for snakes in snake.snake_list[1:]:
        if snake.snake_list[0].distance(snakes) < 10:
            snake.reset_snake()
            score.game_reset()


screen.exitonclick()
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

BOUNDS = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake XVI")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
i = 0
while game_is_on:
    screen.update()

    # Increase speed with score
    if score.score < 3:
        delay = 0.5
    elif score.score > 10:
        delay = 0.1
    else:
        delay = 1/score.score
    # delay = 0.2

    time.sleep(delay)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.enlarge()

    # Detect when going out of bounds
    if snake.head.xcor() > BOUNDS or snake.head.xcor() < -BOUNDS:
        snake.manage_out_of_bounds_x()

    if snake.head.ycor() > BOUNDS or snake.head.ycor() < -BOUNDS:
        snake.manage_out_of_bounds_y()

    # Detect collision with snake
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
            with open("high_score.txt", 'w') as file:
                file.write(str(score.high_score))

screen.exitonclick()

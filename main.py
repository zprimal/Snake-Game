from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

# Create game entities
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

# Establish control scheme
def goLeft():
    snake.goLeft()

def goRight():
    snake.goRight()

def goUp():
    snake.goUp()

def goDown():
    snake.goDown()

screen.onkey(goLeft, "a")
screen.onkey(goRight, "d")
screen.onkey(goUp, "w")
screen.onkey(goDown, "s")

# Start Game
gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food
    if snake.head.distance(food) < 15:
        print("Nom nom")
        food.refresh()
        scoreboard.update()
        snake.extend()

    # Wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        gameOn = False
        scoreboard.gameover()

    # Body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameOn = False
            scoreboard.gameover()

screen.exitonclick()

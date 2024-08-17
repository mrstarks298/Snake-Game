# Import necessary modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the dimensions of the screen
screen.bgcolor("black")  # Set the background color of the screen
screen.title("My Snake Game")  # Set the title of the window
screen.tracer(0)  # Turn off screen updates for better performance

# Create instances of Snake, Food, and Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()  # Start listening for user input
screen.onkey(snake.up, "Up")  # Bind the "Up" key to the snake's up movement
screen.onkey(snake.down, "Down")  # Bind the "Down" key to the snake's down movement
screen.onkey(snake.left, "Left")  # Bind the "Left" key to the snake's left movement
screen.onkey(snake.right, "Right")  # Bind the "Right" key to the snake's right movement

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause for a short time to control the speed of the game
    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random location
        snake.extend()  # Grow the snake
        scoreboard.increase_score()  # Increase the score

    # Detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_on = False  # End the game
        scoreboard.game_over()  # Display the game over message

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            continue  # Skip the head segment
        elif snake.head.distance(segment) < 10:
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display the game over message

# Exit the game when the screen is clicked
screen.exitonclick()

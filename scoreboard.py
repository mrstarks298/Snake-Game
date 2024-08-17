from turtle import Turtle

# Constants for scoreboard text alignment and font
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Creating a Scoreboard class that inherits from the Turtle class
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.score = 0  # Initialize the score to 0
        self.color("white")  # Set the color of the text
        self.penup()  # Lift the pen to avoid drawing lines when moving
        self.goto(0, 270)  # Set the initial position of the scoreboard
        self.hideturtle()  # Hide the turtle cursor
        self.update_scoreboard()  # Display the initial score

    # Method to update the scoreboard display
    def update_scoreboard(self):
        self.clear()  # Clear the previous score display
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Write the current score

    # Method to display the game over message
    def game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Write the game over message

    # Method to increase the score and update the display
    def increase_score(self):
        self.score += 1  # Increase the score by 1
        self.update_scoreboard()  # Update the scoreboard display

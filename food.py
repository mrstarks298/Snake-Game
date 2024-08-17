from turtle import Turtle
import random

# Creating a Food class that inherits from the Turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to prevent drawing lines when the food moves
        # Set the size of the food to be smaller than the default turtle size
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the speed to the fastest (no animation delay)
        self.refresh()  # Place the food at a random position

    # Method to reposition the food at a random location on the screen
    def refresh(self):
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the new random position

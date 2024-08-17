from turtle import Turtle

# Constants for initial snake positions, movement distance, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Creating a Snake class to manage the snake's behavior
class Snake:

    def __init__(self):
        self.segments = []  # List to store the snake's segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The head of the snake is the first segment

    # Method to create the initial snake with predefined segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Add each segment at the starting positions

    # Method to add a new segment to the snake
    def add_segment(self, position):
        new_segment = Turtle("square")  # Create a new segment as a square
        new_segment.color("white")  # Set the color of the segment to white
        new_segment.penup()  # Lift the pen to prevent drawing lines
        new_segment.goto(position)  # Move the segment to the specified position
        self.segments.append(new_segment)  # Add the segment to the list

    # Method to extend the snake by adding a new segment at the end
    def extend(self):
        self.add_segment(self.segments[-1].position())  # Add a new segment at the last segment's position

    # Method to move the snake forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Move each segment to the position of the segment in front of it
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head forward by the defined distance

    # Methods to change the direction of the snake
    def up(self):
        if self.head.heading() != DOWN:  # Ensure the snake doesn't move directly in the opposite direction
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

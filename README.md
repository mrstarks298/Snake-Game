<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=28&duration=3000&pause=1000&color=00FF00&center=true&vCenter=true&width=580&height=50&lines=Classic+Snake+Game;Eat+%F0%9F%9F%A2+Grow+%F0%9F%90%8D+Score+%F0%9F%8F%86" alt="Typing SVG" />
</h1>

This is a classic Snake game implemented in Python using the Turtle graphics library.

## Description

In this game, you control a snake that moves around the screen. The objective is to eat the food (blue circles) that appear randomly on the screen. Each time the snake eats food, it grows longer, and your score increases. The game ends if the snake hits the wall or collides with its own body.

## Features

- Snake movement controlled by arrow keys
- Randomly spawning food
- Score tracking
- Game over condition

## Requirements

- Python 3.x
- Turtle graphics library (comes pre-installed with Python)

## Installation

1. Clone this repository or download the source code.
2. Ensure you have Python 3.x installed on your system.
3. No additional installation is required as the game uses the built-in Turtle graphics library.

## How to Play

1. Run the `main.py` file:
2.Use the arrow keys to control the snake's direction:
- Up arrow: Move up
- Down arrow: Move down
- Left arrow: Move left
- Right arrow: Move right
3. Try to eat the blue food dots to grow the snake and increase your score.
4. Avoid hitting the walls or the snake's own body.
5. The game ends when the snake collides with the wall or itself.

## Project Structure

- `main.py`: The main game loop and setup
- `snake.py`: Contains the Snake class which manages the snake's behavior
- `food.py`: Contains the Food class for spawning and managing food
- `scoreboard.py`: Contains the Scoreboard class for keeping and displaying the score

## Customization

You can customize various aspects of the game by modifying the constants in the respective files:

- Change the game window size in `main.py`
- Adjust snake speed by modifying the `time.sleep()` value in `main.py`
- Change colors, shapes, or sizes in the respective class files

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.

## License

This project is open source and available under the [MIT License](LICENSE).

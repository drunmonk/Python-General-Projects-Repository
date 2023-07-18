# Rock, Paper, Scissors Game

This is a simple implementation of the classic "Rock, Paper, Scissors" game played against the computer. In this game, you can choose either "rock," "paper," or "scissors," and the computer will randomly select one of these options as well. The outcome of the game is determined based on the rules of the game:

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

## How to Play

1. Clone the Repository:
2. Run the Game:

3. Enter Your Choice:
- Type "rock," "paper," or "scissors" (case insensitive) and press Enter.

4. Game Result:
- The program will display the outcome of the game (win, lose, or draw).
- If it's a draw, you can try again.
- If you want to play again, type "Y" and press Enter. Otherwise, type "N" to quit.

## Code Structure

The code is organized into three functions:

1. `game()`: This function initiates the game. It generates the computer's choice and prompts the user for their choice. Depending on the user's choice, it calls `game1()` to handle the game's outcome or `game2()` if the user's choice is invalid.

2. `game1(choices, human_choice, computer_choice)`: This function determines the outcome of the game based on the user's choice and the computer's choice. It uses a `choices` dictionary to define the rules of the game and displays the result accordingly. If the game is a draw, it allows the user to try again. If the user wants to play again, it calls the `game()` function.

3. `game2()`: This function is called when the user's choice is invalid (neither "rock," "paper," nor "scissors"). It informs the user of the invalid input and asks if they want to play again with a valid choice. If the user wants to play again, it calls the `game()` function.

## Requirements

- Python 3.x
- The `random` module is used to generate the computer's choice.


Feel free to fork, modify, and contribute to this project. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

Enjoy playing the game of "Rock, Paper, Scissors" against the computer!


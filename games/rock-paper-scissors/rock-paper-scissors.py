"""
here rock paper scissor is given 1 2 3 numbers 
rock-1 is choosen
case -1
equal-
case -2
won- rock+scissor==1+3=4
case-3
loose-rock+paper==1+2=3
paper-2
case -1
equal-
case -2
won-paper+rock==1+2=3
case-3
loose=paer+scissor==2+3=5
scissor-3
won=sciisor+paper=2+3=5
lose=rock+scissor=1+3=4
each postion in choices list  repersent each posible computer choise  excluding 0
"""


import random

def game():
    # Dictionary containing choices and their corresponding outcomes
    choices = [
        {1: 'rock', 2: 'scissors', 3: 'paper', 'rock': 1, 'scissors': 2, 'paper': 3},
        {3: "you lose", 4: 'you won'},
        {3: "you won", 5: "you lose"},
        {4: "you lose", 5: "you won"}
    ]

    # Computer makes a random choice (1: rock, 2: scissors, 3: paper)
    computer_choice = random.randrange(1, 4)

    # Player enters their choice (rock, paper, or scissors)
    human_choice = input("rock paper scissors: ").strip().lower()

    try:
        game1(choices, human_choice, computer_choice)  # Handle the player's choice
    except:
        game2()  # If the player's choice is invalid, ask if they want to play again

def game1(choices, human_choice, computer_choice):
    # Determine the demi choice based on the player's input
    demi = choices[0][human_choice]

    if demi == computer_choice:
        # If the player's choice and the computer's choice are equal, it's a draw
        print("It's a draw. Try once more.")
        game()
    else:
        # Find the outcome based on the computer's choice and the demi choice
        outcome = choices[computer_choice][demi + computer_choice]
        print(f"{outcome} I chose {choices[0][computer_choice]} and you chose {human_choice}")

        # Ask if the player wants to play again
        flag = input("Do you want to play again? Type Y for yes or N for no: ")
        if flag.lower() == "y":
            game()

def game2():
    # If the player's choice is invalid, inform them and ask if they want to play again
    print("Not a valid input.")
    flag = input("Do you want to play again, this time fair and square? Type Y for yes or N for no: ")
    if flag.lower() == "y":
        game()

game()

"""EX03: Exercise 3: Functional Battleship."""

__author__ = "730394747"

import random


def input_guess(grid_size: int, row_or_column: str) -> int:
    """Inputting grid size and either row guess or column guess."""
    assert row_or_column == "row" or row_or_column == "column"
    if row_or_column == "row":
        row_guess: str = input("Guess a row: ")
        row_number: int = int(row_guess)
        correct: bool = False
        while not correct:   # correct == False
            if row_number > grid_size or row_number <= 0:
                row_guess = str(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
                row_number = int(row_guess)
            else:
                correct = True
        return row_number
    else:  # row_or_column == "column"
        column_guess: str = input("Guess a column: ")
        column_number: int = int(column_guess)
        correct2: bool = False
        while not correct2: 
            if column_number > grid_size or column_number <= 0:
                column_guess = str(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
                column_number = int(column_guess)
            else: 
                correct2 = True
        return column_number


def print_grid(grid_size: int, row_number: int, column_number: int, user_guess: bool) -> None:
    """Printing a grid of boxes to represent the game board."""
    # named constants for colored emoji boxes
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result_box: str = RED_BOX or WHITE_BOX 
    if user_guess is True:
        result_box = RED_BOX
    else: 
        result_box = WHITE_BOX
    # printing a grid
    row_counter: int = 1
    while row_counter <= grid_size:
        emoji_string: str = ""  # string to store the emoji string for a singular row
        column_counter: int = 1  
        if row_number == row_counter:
            while column_counter <= grid_size:
                if column_number == column_counter:
                    emoji_string += result_box
                else: 
                    emoji_string += BLUE_BOX
                column_counter = column_counter + 1
        else:
            while column_counter <= grid_size:
                emoji_string += BLUE_BOX
                column_counter = column_counter + 1
        print(emoji_string)
        row_counter = row_counter + 1
    return 


def correct_guess(secret_row: int, secret_column: int, row_number: int, column_number: int) -> bool:
    """Returning True if Guess is Correct and False if Incorrect."""
    if secret_row == row_number and secret_column == column_number:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Combining all the functions into main function."""
    turn_number: int = 1
    win_status: bool = False
    row_number: int
    column_number: int
    while turn_number <= 5 and win_status is False:
        print(f"=== Turn {turn_number}/5 ===")
        row_number = input_guess(grid_size, "row")
        column_number = input_guess(grid_size, "column")
        win_status = correct_guess(secret_row, secret_column, row_number, column_number)
        print_grid(grid_size, row_number, column_number, win_status)
        if win_status is True:
            print("Hit!")
            print(f"You won in {turn_number}/5 turns!")
        else:
            print("Miss!")
            if turn_number == 5:
                print("X/5 - Better luck next time!")
        turn_number += 1


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
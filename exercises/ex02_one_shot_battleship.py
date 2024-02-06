"""EX02: Exercise 2 -- one shot battleship"""

__author__ = "730394747"

GRID_SIZE: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2
correct: bool = False

# asking the player to pick a row 
row_guess: str = input("Guess a row: ")
row_number: int = int(row_guess)
while not correct: # correct == False
    if row_number > GRID_SIZE:
        row_guess = str(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))
        row_number: int = int(row_guess)
    else:
        correct = True
    
#asking the player to pick a column
column_guess: str = input("Guess a column: ")
column_number: int = int(column_guess)
while correct:
    if column_number > GRID_SIZE:
        column_guess = str(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))
        column_number: int = int(column_guess)
    else: 
        correct = False

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result_box: str = RED_BOX or WHITE_BOX
if row_number == SECRET_ROW and column_number == SECRET_COLUMN:
    result_box = RED_BOX
else:
    result_box = WHITE_BOX

# printing a grid
row_counter: int = 1
while row_counter <= GRID_SIZE:
    emoji_string: str = "" # string to store the emoji string for a singular row
    column_counter: int = 1  
    if row_number == row_counter:
        while column_counter <= GRID_SIZE:
            if column_number == column_counter:
                emoji_string += result_box
            else: 
                emoji_string += BLUE_BOX
            column_counter = column_counter + 1
    else:
        while column_counter <= GRID_SIZE:
            emoji_string += BLUE_BOX
            column_counter = column_counter + 1
    print(emoji_string)
    row_counter = row_counter + 1

#checking for hit or miss
if column_number == SECRET_COLUMN and row_number == SECRET_ROW:
    print("Hit!")
elif column_number == SECRET_COLUMN and row_number != SECRET_ROW:
    print("Close! Correct column, wrong row.")
elif column_number != SECRET_COLUMN and row_number == SECRET_ROW:
    print("Close! Correct row, wrong column.")
else: 
    print("Miss!")
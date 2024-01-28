"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730394747"

# user's turn; turning the str into int for calculations
user_boat: str = input("Pick a secret boat location between 1 and 4: ")
boat_number: int = int(user_boat)

# if user_number < 1, print "Error! user_boat too low!"
if boat_number < 1:
    print("Error! " + user_boat + " too low!")
    exit()
# if user_number > 4, print "Error! user_boat too high!"
if boat_number > 4: 
    print("Error! " + user_boat + " too high!")
    exit()

# opponent's turn; turning the str into int for calculations
opponent_guess: str = input("Guess a number between 1 and 4: ")
opponent_number: int = int(opponent_guess)

# if opponent_number < 1, print "Error! opponent_guess too low!"
if opponent_number < 1:
    print("Error! " + opponent_guess + " too low!")
    exit()
# if opponent_number > 4, print "Error! opponent_guess too high!"
if opponent_number > 4: 
    print("Error! " + opponent_guess + " too high!")
    exit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# printing a string of boxes
if opponent_number == 1 and opponent_number == boat_number:
    print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if opponent_number == 1 and opponent_number != boat_number:
    print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if opponent_number == 2 and opponent_number == boat_number:
    print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
if opponent_number == 2 and opponent_number != boat_number:
    print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
if opponent_number == 3 and opponent_number == boat_number:
    print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
if opponent_number == 3 and opponent_number != boat_number:
    print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
if opponent_number == 4 and opponent_number == boat_number:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
if opponent_number == 4 and opponent_number != boat_number:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)

# checking for equality
if opponent_number == boat_number:
    print("Correct! You hit the ship.")  
else: 
    print("Incorrect! You missed the ship.")

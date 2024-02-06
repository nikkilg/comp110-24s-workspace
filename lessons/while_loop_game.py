"""number guessing name"""

from random import randint
SECRET: int = randint(1,10) # cannot put this inside the while loop because it would keep coming up with a new secret number
correct: bool = False

while not correct: # correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else: 
        print(f"Try again. {guess} is not the secret number.")
    
    # giving a hint by stating if guess is too high or too low
    if guess > SECRET:
        print("That guess is too high.")
    if guess < SECRET:
        print("That guess is too low.")

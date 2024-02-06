"""practice using elif"""

secret: int = 2

# old way of doing things with individual if and else statements
if secret == 10:
    print("Correct!")
else:
    if secret < 10:
        print("Your guess was too low.")
    else:
        print("Your guess was too high.")

# combining lines 5 and 6 to make an elif statement
if secret == 10:
    print("Correct!")
elif secret < 10:
    print("Your guess was too low.")
else:
    print("Your guess was too high.")
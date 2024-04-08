"""EX08 Set-Up: Turtle Tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

# lines (distance) and turning (degrees)
# leo.forward(50)
# leo.left(30)
# leo.right(40)

# using lines and turns to make a square
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)

# to repeat something a certain number of times: while (<counter_variable> < <number_of_times>):
# i: int = 0
# while (i < 4):
    # leo.forward(300)
    # leo.left(90)
    # i = i + 1

# to move the turtle to a new x, y position: <turtlevariable>.goto(<x_coordinate>,<y_coordinate>):
leo.penup()
leo.goto(-250, -250)
leo.pendown()

# to change the color with RGB values: <turtlevariable>.color(<red>, <green>, <blue>)
leo.color(30, 42, 152)

# using while loops and lines/turns to make a triangle
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(500)
    leo.left(120)
    i = i + 1

leo.end_fill()
leo.speed(50)
leo.hideturtle()

# beginning new turtle to do the rest of the work
bob: Turtle = Turtle()
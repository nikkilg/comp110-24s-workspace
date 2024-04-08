"""EX08: Using Recursion to Draw Forest Scene & Attempting Extra 15%."""

# Trying something not in the turtle tutorial (circle function), and a scene more complex than 4 components
# Also breaking up complex functions (draw_tree) into two simpler functions (draw_trunk and draw_branches)

__author__ = "730394747"

from turtle import Turtle, colormode, done
colormode(255)


# main function that calls all other functions to draw scene
def main() -> None:
    """The entrypoint of my forest scene."""
    turtle1: Turtle = Turtle()
    draw_moon(turtle1, 400.0, 200.0, 75.0)
    draw_ground(turtle1, -600.0, -300.0, 1200.0, 20.0)
    # calling a function multiple times
    draw_tree(turtle1, -400.0, -300.0)
    draw_tree(turtle1, -75.0, -300.0)
    draw_tree(turtle1, 250.0, -300.0)
    turtle1.hideturtle()
    done()


def draw_moon(turtle1: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle of the given radius starting at location x, y."""
    # getting turtle to correct starting location
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.pendown()
    # setting outline color and fill color
    turtle1.pencolor("blue")
    turtle1.fillcolor(209, 210, 218)
    # drawing the circle for the moon
    turtle1.begin_fill()
    turtle1.circle(radius)
    turtle1.end_fill()


def draw_ground(turtle1: Turtle, x: float, y: float, length: float, height: float) -> None:
    """Draw a rectangle of the given length whose top-left corner is located at x, y."""
    # getting turtle to correct starting location
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.pendown()
    # setting outline color and fill color
    turtle1.pencolor("brown")
    turtle1.fillcolor(62, 29, 6)
    # drawing the rectangle for the ground
    turtle1.begin_fill()
    i: int = 0
    while (i < 2):
        turtle1.forward(length)
        turtle1.right(90)
        turtle1.forward(height)
        turtle1.right(90)
        i = i + 1
    turtle1.end_fill()


def draw_trunk(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose bottom-right corner is located at x, y."""
    # getting turtle to correct starting location
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.pendown()
    # setting outline color and fill color
    turtle1.pencolor("brown")
    turtle1.fillcolor(84, 52, 30)
    # drawing the square for the trunk
    turtle1.begin_fill()
    i: int = 0
    while (i < 4):
        turtle1.forward(width)
        turtle1.left(90)
        i = i + 1
    turtle1.end_fill()

    
def draw_branches(turtle1: Turtle, x: float, y: float, length: float, counter: int) -> None:
    """Recursive function: Draw three triangles stacked to make branches -- first triangle has top corner at x,y."""
    # getting turtle to correct starting location
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.left(240)
    turtle1.pendown()
    # setting outline color and fill color
    turtle1.pencolor(26, 112, 33)
    turtle1.fillcolor(26, 112, 33)
    # drawing the initial triangle for the tree branches
    turtle1.begin_fill()
    i: int = 0
    while (i < 3):
        turtle1.forward(length)
        turtle1.left(120)
        i = i + 1
    turtle1.end_fill()
    turtle1.left(120)
    # recursion for stacking tree branches
    if counter >= 2:
        return None
    else:
        return draw_branches(turtle1, x, y + 75.0, length * 0.8, counter + 1)
    

def draw_tree(turtle1: Turtle, x: float, y: float) -> None:
    """Simplifying functions: Draw a tree by calling the draw_trunk and draw_branches functions."""
    # code for drawing one tree with given x, y values
    draw_trunk(turtle1, x, y, 50.0)
    draw_branches(turtle1, x + 25.0, y + 300.0, 300.0, 0)


if __name__ == "__main__":
    main()
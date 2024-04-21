"""CQ08: Object-Oriented Programming with Point Class."""

from __future__ import annotations
# for defining a method that returns its own type (e.g. a method in our Point class that returns a Point)

__author__ = "730394747"


class Point:
    """Making a new class called Point."""
    # creating attributes x and y 
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Setting initial values for x and y attributes."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutating Method: Point#scale_by."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Mutating Method: Point#scale."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self):
        """Magic method: print prettier version of point."""
        return f"({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        """Magic method: overriding multiplication."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __getitem__(self, index: int) -> float:
        """Overloading subscription notation: being able to index Point even though it's not a list."""
        if index == 0: 
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError

        
a: Point = Point(1.0, 2.0)
print(str(a))
b: Point = a.scale(3.0)

# due to the __mul__ function, it now knows what "*" means and can multiply instead of giving an error
# a is corresponding with self and 3.0 is corresponding with factor 
b: Point = a * 3.0
print(b)
print(f"My point is: {b}")

# due to __getitem__, can now print y coordinate when calling b[1]
print(b[1])
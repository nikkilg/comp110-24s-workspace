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
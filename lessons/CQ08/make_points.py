"""CQ08: Checking Methods for correctness."""

__author__ = "730394747"

from point import Point

point1: Point = Point(2.0, 4.0)

point1.scale_by(2)
print(point1.x)
print(point1.y)

point1.scale(2)
print(point1.x)
print(point1.y)
"""File to define Fish class."""

__author__ = "730394747"


class Fish:
    """Fish class."""
    # attributes for Fish class
    age: int
    
    def __init__(self):
        """__init__ for Fish class."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increasing the age per day."""
        self.age += 1
        return None
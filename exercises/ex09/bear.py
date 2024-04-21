"""File to define Bear class."""

__author__ = "730394747"


class Bear:
    """Bear class."""
    # attributes for Bear class
    age: int
    hunger_score: int
    
    def __init__(self):
        """__init__ for Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Increasing the age and decreasing the hunger score per day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increasing the hunger score by number of fish eaten."""
        self.hunger_score += num_fish
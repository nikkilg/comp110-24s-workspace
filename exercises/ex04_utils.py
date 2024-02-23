"""Exercise 4: list Utility Functions."""

__author__ = "730394747"

def all(my_list: list[int], number1: int) -> bool:
    idx: int = 0
    while idx < len(my_list):
        for item in my_list:
            if item == number1:
                return True 
            else: 
                return False
        idx += 1
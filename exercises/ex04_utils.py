"""Exercise 4: list Utility Functions."""

__author__ = "730394747"


def all(my_list: list[int], number1: int) -> bool:
    """List that returns bool if numbers are equal."""
    if len(my_list) == 0:
        return False
    for item in my_list:
        if item != number1: 
            return False
    return True


def max(my_list: list[int]) -> int:
    """List that returns maximum from a list."""
    if len(my_list) == 0:
        raise ValueError("max() arg is an empty List")
    largest: int = my_list[0]
    for item in my_list:
        if item > largest:
            largest = item
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checking for equality of two lists."""
    if len(list1) != len(list2):
        return False
    idx: int = 0
    for item in list1:
        if list1[idx] == list2[idx]:
            idx += 1
        else: 
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Appending one list to another list."""
    idx: int = 0
    while idx < len(list2):
        list1.append(list2[idx])
        idx += 1
    return
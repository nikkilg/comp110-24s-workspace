"""Mutating functions."""

__author__ = "730394747"


# Part 1 = manual_append()
def manual_append(list1: list[int], number1: int) -> None:
    """Appending a number to the list."""
    list1.append(number1)


# Part 2 = double
def double(list2: list[int]) -> None:
    """Doubling each number in the list."""
    idx: int = 0
    while idx < len(list2):
        list2[idx] *= 2
        idx += 1

#  from lessons.mutate import manual.append <-- this is how you call the function in the REPL
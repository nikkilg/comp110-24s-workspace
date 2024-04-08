"""Functions that implement sorting algorithms."""

__author__ = "730394747"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sorted_idx: int = 0
    while sorted_idx < len(x) - 1:
        unsorted_idx: int = sorted_idx + 1
        while unsorted_idx > 0:
            if x[unsorted_idx - 1] > x[unsorted_idx]:
                placeholder: int = x[unsorted_idx - 1]
                x[unsorted_idx - 1] = x[unsorted_idx]
                x[unsorted_idx] = placeholder
            unsorted_idx -= 1
        sorted_idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    counter1: int = 0
    while counter1 < len(x):
        counter2: int = counter1
        min_idx: int = counter1
        while counter2 < len(x):
            if x[min_idx] > x[counter2]:
                min_idx = counter2
            counter2 += 1
        if x[counter1] > x[min_idx]:
            placeholder: int = x[counter1]
            x[counter1] = x[min_idx]
            x[min_idx] = placeholder
        counter1 += 1
    return None
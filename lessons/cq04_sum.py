"""CQ04 -- Summing elements of a list using different loops."""

__author__ = "730394747"


# while loop
def w_sum(vals: list[float]) -> float:
    """Sum of list using a while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


# for loop
def f_sum(vals: list[float]) -> float:
    """Sum of list using a for... in... loop."""
    sum: float = 0.0
    for item in vals:
        sum += item
    return sum


# for loop with range
def f_range_sum(vals: list[float]) -> float:
    """Sum of list using a for loop and range."""
    sum: float = 0.0
    for item in range(0, len(vals)):
        sum += vals[item]
    return sum
"""CQ07: Writing a Recursive Function."""

__author__ = "730394747"

# standard function
# f(n, k) = n × k, with recursion on n ≥ 0


def f(n: int, k: int) -> int:
    """Creating recursive rule for standard function."""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return k + f(n - 1, k)
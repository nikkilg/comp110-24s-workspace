"""LS21 - sum all elements in a list."""


def sum(elements: list[int]) -> int:
    """Sum all elements in list named elements."""
    total: int = 0
    for item in elements:
        total += item
    return total
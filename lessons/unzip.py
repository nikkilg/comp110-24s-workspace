"""Splitting a dictionary into two lists."""

__author__ = "730394747"


def get_keys(test: dict[str, int]) -> list[str]: 
    """Dictionary as input and returning list of keys."""
    my_list: list[str] = []
    for key in test: 
        my_list.append(key)
    return my_list


def get_values(test: dict[str, int]) -> list[int]:
    """Dictionary as input and returning list of values."""
    my_list: list[int] = []
    for key in test:
        my_list.append(test[key])
    return my_list
"""LS22 - Functions that either mutate a list or don't."""


def remove_first(my_list: list[str]) -> None:
    """Remove first element of the list."""
    my_list.pop(0)


def get_first(my_list: list[str]) -> str:
    """Return first element of the list without mutating."""
    return my_list[0]


def get_and_remove_first(my_list: list[str]) -> str:
    """Return first element of the list and remove it from the list."""
    elem: str = my_list[0]
    my_list.pop(0)
    return elem
"""EX05 -- Dictionary Functions."""

__author__ = "730394747"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values."""
    key: str = ""
    value: str = ""
    newdict: dict[str, str] = dict()
    for key in dictionary:
        value = dictionary[key]
        newdict[value] = key
    if len(dictionary) != len(newdict):
        raise KeyError("Cannot have two identical keys!")
    return newdict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returning most frequent favorite color."""
    name: str = ""
    favorite_color: str = ""
    counter: int = 0
    colordict: dict[str, int] = dict()
    # adding number of times color was mentioned
    for name in dictionary:
        favorite_color = dictionary[name]
        if favorite_color in colordict:
            counter = colordict[favorite_color] + 1
        else: 
            counter = 1
        colordict[favorite_color] = counter
    # returning most popular color 
    largest: int = 0
    popular_color: str = ""
    for favorite_color in colordict:
        counter = colordict[favorite_color]
        if counter > largest:
            largest = counter
            popular_color = favorite_color
    return popular_color


def count(my_list: list[str]) -> dict[str, int]:
    """Counting number of times an object appears in a list."""
    newdict: dict[str, int] = dict()
    counter: int = 0 
    for item in my_list:
        if item in newdict:
            counter = newdict[item] + 1
        else: 
            counter = 1
        newdict[item] = counter
    return newdict


def alphabetizer(my_list: list[str]) -> dict[str, list[str]]:
    """List of words that begin with a specific letter."""
    newdict: dict[str, list[str]] = dict()
    new_list: list[str] = []
    for item in my_list: 
        lower = item.lower()
        if lower[0] in newdict:
            newdict[lower[0]].append(lower)
        else:
            new_list = [lower]
            newdict[lower[0]] = new_list
    return newdict


def update_attendance(og_dict: dict[str, list[str]], week: str, student: str) -> None:
    """Updating attendance information."""
    student_list: list[str] = []
    if week in og_dict:
        student_list = og_dict[week]
        if student not in student_list:
            student_list.append(student)
    else:
        student_list.append(student)
        og_dict[week] = student_list
    return None
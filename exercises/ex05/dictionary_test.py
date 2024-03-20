"""EX06 -- Unit Tests for EX05 dictionary functions."""

__author__ = "730394747"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# unit tests for invert function
def test_invert_use_case1() -> None:
    """Basic use case for invert function: inverting month and year in a dictionary."""
    dictionary: dict[str, str] = {"March": "2024", "September": "2001"}
    newdict: dict[str, str] = invert(dictionary)
    assert newdict == {"2024": "March", "2001": "September"}


def test_invert_use_case2() -> None:
    """Basic use case for invert function: Inverting first and last name in a dictionary."""
    dictionary: dict[str, str] = {"Joe": "Biden"}
    newdict: dict[str, str] = invert(dictionary)
    assert newdict == {"Biden": "Joe"}


def test_invert_edge_case() -> None:
    """Edge case for invert function: when key and value are the same word but one is capitalized."""
    dictionary: dict[str, str] = {"brown": "Brown"}
    newdict: dict[str, str] = invert(dictionary)
    assert newdict == {"Brown": "brown"}


# unit tests for favorite_color function
def test_fav_color_use1() -> None:
    """Basic use case for favorite color function: blue as favorite color."""
    dictionary: dict[str, str] = {"Bob": "blue", "Don": "blue", "Tammy": "purple"}
    return_value: str = favorite_color(dictionary)
    assert return_value == "blue"


def test_fav_color_use2() -> None:
    """Basic use case for favorite color function: pink as favorite color."""
    dictionary: dict[str, str] = {"Sam": "pink", "Don": "blue", "Tammy": "purple", "Lexi": "pink"}
    return_value: str = favorite_color(dictionary)
    assert return_value == "pink"


def test_fav_color_edge() -> None:
    """Edge case for favorite color function: all colors mentioned one time."""
    dictionary: dict[str, str] = {"Sam": "purple", "Don": "blue", "Tammy": "pink"}
    return_value: str = favorite_color(dictionary)
    assert return_value == "purple"  # when every color is mentioned once, should return first color mentioned


# unit tests for count function
def test_count_use1() -> None:
    """Basic use case for count function: ice cream flavors."""
    ice_cream: list[str] = ["chocolate", "vanilla", "chocolate", "strawberry", "mint chocolate chip", "cookies and cream", "vanilla"]
    return_dict: dict[str, int] = count(ice_cream)
    assert return_dict == {"chocolate": 2, "vanilla": 2, "strawberry": 1, "mint chocolate chip": 1, "cookies and cream": 1}


def test_count_use2() -> None:
    """Basic use case for count function: pets."""
    pets: list[str] = ["dog", "dog", "cat", "dog", "rabbit", "fish", "fish", "cat", "dog"]
    return_dict: dict[str, int] = count(pets)
    assert return_dict == {"dog": 4, "cat": 2, "fish": 2, "rabbit": 1}


def test_count_edge() -> None:
    """Edge case for count function: no items in the list."""
    my_list: list[str] = []
    return_dict: dict[str, int] = count(my_list)
    assert return_dict == {}


# unit tests for alphabetizer function
def test_alphabetizer_use1() -> None:
    """Basic use case for alphabetizer function: first names that are originally capitalized."""
    names: list[str] = ["John", "Sam", "Lila", "Simon"]
    return_dict: dict[str, list[str]] = alphabetizer(names)
    assert return_dict == {"j": ["John"], "s": ["Sam", "Simon"], "l": ["Lila"]}


def test_alphabetizer_use2() -> None:
    """Basic use case for alphabetizer function: plant names where some are capitalized and some are not."""
    plants: list[str] = ["Chrysanthemum", "rose", "marigold", "carnation", "Lily"]
    return_dict: dict[str, list[str]] = alphabetizer(plants)
    assert return_dict == {"c": ["Chrysanthemum", "carnation"], "r": ["rose"], "m": ["marigold"], "l": ["Lily"]}


def test_alphabetizer_edge() -> None:
    """Edge case for alphabetizer function: string in list has multiple words."""
    states: list[str] = ["Virginia", "North Carolina", "South Carolina"]
    return_dict: dict[str, list[str]] = alphabetizer(states)
    assert return_dict == {"v": ["Virginia"], "n": ["North Carolina"], "s": ["South Carolina"]}


# unit tests for update_attendance
def test_update_attendance_use1() -> None:
    """Basic use case for update attendance function: weekday is already in dictionary."""
    dictionary: dict[str, list[str]] = {"Wednesday": ["Abby", "John"]}
    week: str = "Wednesday"
    student: str = "Nikki"
    update_attendance(dictionary, week, student)
    assert dictionary == {"Wednesday": ["Abby", "John", "Nikki"]}


def test_update_attendance_use2() -> None:
    """Basic use case for update attendance function: weekday is not already in dictionary."""
    dictionary: dict[str, list[str]] = {"Wednesday": ["Abby", "John"]}
    week: str = "Thursday"
    student: str = "Nikki"
    update_attendance(dictionary, week, student)
    assert dictionary == {"Wednesday": ["Abby", "John"], "Thursday": ["Nikki"]}


def test_update_attendance_edge() -> None:
    """Edge case for update attendance function: day of the week has no students."""
    dictionary: dict[str, list[str]] = {}
    week: str = "Thursday"
    student: str = ""
    update_attendance(dictionary, week, student)
    assert dictionary == {"Thursday": [""]}

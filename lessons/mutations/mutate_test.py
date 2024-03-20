"""LS23 - Test my mutate functions."""

# importing functions from the mutate_functions file 
from lessons.mutations.mutate_functions import remove_first
from lessons.mutations.mutate_functions import get_first
from lessons.mutations.mutate_functions import get_and_remove_first


def test_remove_first_use_case() -> None:
    """Test basic use case for remove first function."""
    test: list[str] = ["cloudy", "rainy", "sunny"]
    remove_first(test)
    assert test == ["rainy", "sunny"]


def test_get_first_use_case() -> None:
    """Test basic use case for get first function."""
    test: list[str] = ["cloudy", "rainy", "sunny"]
    return_value: str = get_first(test)
    # testing that the list is not mutated
    assert test == ["cloudy", "rainy", "sunny"]
    # testing that return value is first item in list
    assert return_value == "cloudy"


def test_get_and_remove_first_use_case() -> None:
    """Test basic use case for get and remove function."""
    test: list[str] = ["cloudy", "rainy", "sunny"]
    return_value: str = get_and_remove_first(test)
    # testing that return value is first item in list
    assert return_value == "cloudy"
    # testing that list was successfully mutated
    assert test == ["rainy", "sunny"]
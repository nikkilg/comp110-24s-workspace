"""Test my garden functions."""

__author__ = "730394747"

# importing functions from other file
from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


# use case for add_by_kind function
def test_add_by_kind_use() -> None:
    """Test basic use case for add by kind function."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "lily"]}
    new_plant_kind: str = "tree"
    new_plant: str = "fir"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {"flower": ["marigold", "lily"], "tree": ["fir"]}


# edge case for add_by_kind function
def test_add_by_kind_edge() -> None:
    """Test edge case for add by kind function: empty dictionary should return empty dictionary."""
    by_kind: dict[str, list[str]] = {}
    new_plant_kind: str = ""
    new_plant: str = ""
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {"": [""]}


# use case for add_by_date function
def test_add_by_date_use() -> None:
    """Test basic use case for add by date function."""
    by_date: dict[str, list[str]] = {"June": ["rose", "lily"], "July": ["marigold"]}
    month: str = "August"
    plant: str = "rosemary"
    add_by_date(by_date, month, plant)
    assert by_date == {"June": ["rose", "lily"], "July": ["marigold"], "August": ["rosemary"]}


# edge case for add_by_date function
def test_add_by_date_edge() -> None:
    """Test edge case for add by date function: empty dictionary should return empty dictionary."""
    by_date: dict[str, list[str]] = {}
    month: str = ""
    plant: str = ""
    add_by_date(by_date, month, plant)
    assert by_date == {"": [""]}


# use case for lookup_by_kind_and_date function
def test_lookup_by_kind_and_date_use() -> None:
    """Test basic use case for lookup by kind and date function."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "lily"], "tree": ["fir"]}
    by_date: dict[str, list[str]] = {"June": ["rose", "lily"], "July": ["marigold"], "August": ["rosemary"]}
    plant_kind: str = "flower"
    month: str = "July"
    return_value: str = lookup_by_kind_and_date(by_kind, by_date, plant_kind, month)
    assert return_value == f"{plant_kind} to plant in {month}: {['marigold']}"


# edge case for lookup_by_kind_and_date function
def test_lookup_by_kind_and_date_edge() -> None:
    """Test edge case for lookup by kind and date function -- no plants to plant during a specific month."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "lily"], "tree": ["fir"]}
    by_date: dict[str, list[str]] = {"June": ["rose", "lily"], "July": ["marigold"], "August": ["rosemary"], "September": []}
    plant_kind: str = "flower"
    month: str = "September"
    return_value: str = lookup_by_kind_and_date(by_kind, by_date, plant_kind, month)
    assert return_value == f"No {plant_kind} to plant in {month}"

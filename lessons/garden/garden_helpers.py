"""Some functions for my garden plan!"""

__author__ = "730394747"

# by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
# new_plant: str = "daisy"
# new_plant_kind: str = "flower"


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Adding plant to dictionary and sorting by plant type."""
    if new_plant_kind in by_kind:   # if plant kind is already in the list
        by_kind[new_plant_kind].append(new_plant)
    else:   # if plant kind is not already in the list
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)


def add_by_date(by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Adding plant to dictionary and sorting by month."""
    if month in by_date:
        by_date[month].append(plant)
    else:
        by_date[month] = []
        by_date[month].append(plant)


def lookup_by_kind_and_date(by_kind: dict[str, list[str]], by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Return string with list of plants of a specific kind to plant in a specific month."""
    assert plant_kind in by_kind
    assert month in by_date
    kind_list: list[str] = by_kind[plant_kind]
    month_list: list[str] = by_date[month]
    combo_list: list[str] = []
    # go through both lists and find elements that appear in both
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:  # plant is in the kind list and the month list
                combo_list.append(plant)
    if len(combo_list) > 0:
        return f"{plant_kind} to plant in {month}: {combo_list}"
    else: 
        return f"No {plant_kind} to plant in {month}"
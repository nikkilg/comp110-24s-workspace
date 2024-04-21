"""File to define River class."""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

__author__ = "730394747"


class River:
    """River class."""
    day: int   # tells you what day of the river’s lifecycle you are modeling
    fish: list[Fish]  # river’s bear population
    bears: list[Bear]   # river’s fish population
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removing animals from the river as they age."""
        # creating new lists to append animals that aren't too old. 
        updated_bear_list: list[Bear] = []
        updated_fish_list: list[Fish] = []
        for x in self.fish:
            if x.age <= 3: 
                updated_fish_list.append(x)
        for x in self.bears:
            if x.age <= 5:
                updated_bear_list.append(x)
        # setting new lists equal to self.bears and self.fish
        self.bears = updated_bear_list
        self.fish = updated_fish_list
        return None
    
    def remove_fish(self, amount: int):
        """Removing fish at index 0 a given amount of times."""
        counter: int = 0
        while counter < amount: 
            self.fish.pop(0)
            counter += 1

    def bears_eating(self):
        """Removing 3 fish for each bear if there are at least 5 fish in the river."""
        for x in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                x.eat(3)      
        return None
    
    def check_hunger(self):
        """Removing bears that starve and adding surviving bears to new list."""
        surviving_bears: list[Bear] = []
        for x in self.bears:
            if x.hunger_score >= 0:
                surviving_bears.append(x)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Adding four new fish for every two fish in the list."""
        baby_fish: int = (len(self.fish) // 2) * 4
        counter: int = 0
        while counter < baby_fish:
            self.fish.append(Fish())
            counter += 1
        return None
    
    def repopulate_bears(self):
        """Adding one new bear for every two bears in the list."""
        baby_bears: int = len(self.bears) // 2
        counter: int = 0
        while counter < baby_bears:
            self.bears.append(Bear())
            counter += 1
        return None
    
    def view_river(self):
        """Viewing the fish and bear populations in the river on a given day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week in the river by calling one_river_day 7 times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

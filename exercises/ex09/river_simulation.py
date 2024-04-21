"""EX09: River Simulation Using Classes."""

from exercises.ex09.river import River

__author__ = "730394747"

my_river: River = River(10, 2)

# testing functionality of view_river by calling it 
my_river.view_river()

# testing functionality of one_river_week by calling it
my_river.one_river_week()
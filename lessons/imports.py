"""File containing imported stuff."""

# importing modules lesson
from lessons import my_functions

# if __name__ == "__main__": 
print(my_functions.add(4,5))
print(my_functions.my_variable)

# ls18 gradescope question
from lessons.my_functions import double, double_display

print(double(1))
double_display(4)
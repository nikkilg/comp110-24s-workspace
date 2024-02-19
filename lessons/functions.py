"""example functions to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """returns the maximum value out of two numbers"""
    if number1 >= number2:
        return number1
    else: # number1 is less than number2
        return number2

max_number: int = my_max(1,10)
other_max: int = my_max(11, 3)
print(max_number)
print(other_max)

"""practice writing functions in class"""

def mimic(my_words: str) -> str:
    """given the string my_words, outputs the same string"""
    return my_words
mimic("Hello!")
print(mimic("Hello!"))

my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)
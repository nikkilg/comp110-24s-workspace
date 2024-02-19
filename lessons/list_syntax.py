"""demonstrate basic list syntax."""

# initialize an empty list (lines 4 and 5 are doing the same thing)
grocery_list: list[str] = list()  # <-- list constructor
grocery_list: list[str] = []  # <-- this is called a literal

print(grocery_list)

# add item to the list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
print("After appending: ")
print(grocery_list)

# create an already populated list   <-- this would replace lines 4-12
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Already populated list: ")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

# indexing in a list
print("Print first element of string: ")
print(grocery_list[0])

# modifying list item by indexing
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change: ")
print(grocery_list)

# can have duplicates in a list
grocery_list.append("almond milk")
print("Adding a duplicate to the list: ")
print(grocery_list)

# measuring length of a list
print("Length of grocery list: ")
print(len(grocery_list))

# removing an item from the list
grocery_list.pop(3)
print("After removing almond milk: ")
print(grocery_list)

# function using list as argument
print("~*~ Functions! ~*~")
def display(word: list[str]) -> None:  # adding none means you're not returning anything; could also just add a colon after parameters
    print(word)

display(grocery_list)
display(["Alyssa", "Nikki", "Suzy"])  # this is calling the function to a different list

# assigning the function to a variable; what will return?
x = display(["Alyssa", "Nikki", "Suzy"])
print(x)  # this will print "None" because function doesn't have a return value

# create a list within a function
def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list

print(create("Hello", "World"))
# OR
x: list[str] = create("Hello", "World")
print(x)  # this works because the function now has a return value
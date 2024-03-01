"""Practice using for loops with dictionary."""

# print all with value True
in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}
for key in in_stock:
    # key is "carrots", "beets", "apples"
    # in_stock[key] is values: True, False, True
    if in_stock[key] == True:   # can also just say if in_stock[key]
        print(key)
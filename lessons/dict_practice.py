"""Practice Using Dictionary."""

# two ways to initialize a dictionary
ice_cream1: dict[str, int] = dict()  # can leave dictionary empty to start like this or enter values like line 5
ice_cream2: dict[str, int] = {'chocolate': 12, 'vanilla': 8, 'strawberry': 5}  # can use double or single quotes

# after adding mint
print("After adding mint:")
ice_cream2["mint"] = 3
print(ice_cream2)

# after removing mint
print("After removing mint:")
ice_cream2.pop("mint")
print(ice_cream2)

# accessing a value from a key in the dictionary
print("Checking value of vanilla:")
print(ice_cream2["vanilla"])
print(f"{ice_cream2['vanilla']}")    # printing using a f string and a dictionary

# updating a value in dictionary 
print("Updating the value of vanilla:")
ice_cream2["vanilla"] = 9
ice_cream2["vanilla"] += 1
print(ice_cream2)

# checking if in dictionary
print("Checking if key is in dictionary:")
print("mint" in ice_cream2)
print("chocolate" in ice_cream2)
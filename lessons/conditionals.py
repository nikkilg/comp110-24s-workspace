"""demonstrating conditionals"""

user_input: str = input("Pick a number: ")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))

# if user_number < 10, print "small"
if user_number < 10:
    print("small")
else: # user_number >= 10
   print("big") 

# if a number is even, print even   
if user_number % 2 == 0:
    print("even")
else: # user_number is odd
    print("odd")

print(user_number)
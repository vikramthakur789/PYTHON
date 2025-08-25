# built-it DS that stores an ordered, mutable collection of items 
# Lists can hold items of any type, including other lists


# Ordered: Items have a defined order and can be accessed by their index.
# Mutable: You can change, and, or remove item after the list has been create.
# Heteogeneous: A single list can contain elements of diferent data types.
# Iterable: Lists can be looped over using for loops or comprehensior.

my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", 3.66, True] 
nested = [[1,2], [3,4]]

# Empty list
empty = []

# List of string
colors = ['red', 'green', 'blue']

# List of booleans 
flags = [True, False, True]

# List of mixed types
info = ["Alice", 30, 3.7, False]

# List inside a list (nested)
matrix = [[1,2], [3,4], [5,6]]

li = list("HELLO")
print(li)

s = {10, 20, 30}
lst = list(s)
print(lst)

print (list( range(10)))
original_list = [3,4,5,2,273]

copied_list = list[original_list]
print(copied_list)

number = [10, 20, 30, 40, 50]
# list[strat:end:step]
print(number[1:4])
print(number[1::2])
print(number[1:22]) # mo error
print(number[len(number) - 1])
print(number[::-1])
print(number[-3:])


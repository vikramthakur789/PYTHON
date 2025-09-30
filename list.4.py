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
print(number[-3 :])

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits) 

fruits.append("mango")
print(fruits)   # [ ' apple' ,'blueberry', 'cherry', 'mango']

fruits.insert(2, "mango")
print(fruits)  # [ ' apple' ,' blueberry' , 'mango' , 'cherry' , 'mango' ]

fruits_2 = ["grapes", "kiwi"]
fruits.extend(fruits_2) # append would add the entire list as a single element
print(fruits)  #[ apple' ,'blueberry', 'mango', 'cherry', 'mango', 'grapes', 'kiwi

fruits.remove("apple")
print(fruits)  #[ 'blueberry', 'mango', 'cherry', 'mango', 'grapes',]

fruits.pop()
print(fruits)

fruits.pop(3)
print(fruits)

fruits.pop(-2) # default -1 
print(fruits)
print(fruits.pop(-2))

del fruits[1:3]
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits[1:3] = ["bluberry", "kiwi"]
print("*******",fruits)

fruits.clear()
print(fruits) #[]

# shallow vs deep copy
a = [1,2,3]
b = a[:] # shallow copy of a flat list
b.append(4) 
print(a) # [1,2,3]
print(b) # [1,2,3,4]

a = [[1,2],
     [3,4]]
print(a[0][1],a[1][0])

a = [[1,2],[3,4]]
b = a[:]
b[0][0] = 99
a[1][0] = 99
a[1][1] = 99
print(b)
print(a)
print(id(a[0]), id(b[0]))

import copy
b = copy.deepcopy(a)
print(id(a[0]), id(b[0]))
b[0] [0] = 99
print(b)
print(a)

a = [1, 2, 3, 4]
b = [5, 6]
result = a + b + [7]
print(result)

a = [9, 9]
print(a*4)

a = [0] * 5
print(a)

fruits = ['apple','mango','banana']
print('mango' in fruits) # linear search
print('mango' in fruits)
print('he' in 'hello')

nested = [[0]*2] * 4
nested[0][1] = 1
print(nested)

# function for list
print(len([1,2,3,[4,5]]))
number = [2,5,2,5,7,8]
print(min(number))
print(max(number))
print(sum(number))

name= ['Alice', 'ALice', 'vikram']
print(min(name))
print(max(name))
print(ord('l'), ord('L'))

# sort
nums = [1, 2, 3]
nums.reverse() # reversed
print(nums)
print(list(reversed(nums)))

fruits = ['banana', 'apple', 'cherry']
# my_list.sort(key=None, revsers=False)
fruits.sort( key=len, reverse=True)
print(fruits)

fruits = ['banana', 'apple', 'cherry']
sorted_fruits = sorted(fruits)
print(sorted_fruits)

nums = [-26,26,-126,3,4,56]
nums.sort(key = abs)
print(nums)

name = ['Alice', 'ALice', 'vikram']
print(sorted(name, key=str.lower, reverse=True))

fruits = ['banana', 'apple', 'cherry', 'orange', 'apple']
print(fruits[1:2].count('apple'))
print(fruits.count('kiwi'))
print(fruits.index('banana',0))

for fruit in fruits:
    print(fruit)
print()
for i in range(len(fruits)):
    print(fruits[i])    

c = 0
for fruit in fruits:
    if fruit == 'apple':
        c += 1
print(c)
f_index = 0
for i in range(len(fruits)):
    if fruits[i] == 'orange':
        f_index = i
        break
print(f_index)   

reveresed_list = []
for i in range(len(fruits) -1, -1, -1):
    reveresed_list.append(fruits[i])
print(reveresed_list)    

nums = [4,3,2,5,6,7,34,1]
min_num = nums[0] #4
for i in nums:
    if  min_num > i:
        min_num = i
print(min_num) #1        

# Nested list

numbers = [1,2,3,4]

print("hello")

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    # row = [1,2,3]
    for x in row:
        print(x)

names = ['golu', 'vikram', 'golu', 'vikram', 'vikram']
print(names[1:2].count('vikram'))
print(names.count('virkam'))
print(names.index('golu',0))


print(min(name))
print(max(name))
print(ord('l'), ord('L'))

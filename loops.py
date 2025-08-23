'''
while condition:
     # code block to be executed

1. Python checks the condition.
2. If its True, it executes the indented block.
3. After the block runs, it re-checks the condition.
4. If its still True, it repeats.
5. If it becomes False, the loop stop.

'''

x = 1
while x <= 5:
    print('Hello World', x)
    x += 1
    if x == 4:
        break

X = 1
while True:
    print('OK')
    X += 1
    if x == 4:
        break    

x = 10
while x >= 1:
    print(x)
    x -= 1    

x = 1
while x <= 10:
    print(x)
    x += 1    


# for loop
'''
for variable in sequence:
    # Code block (loop body

 '''

fruits = ['apple', 'banana', 'cherry']
print(fruits[2])
for x in fruits:
    print(x)

name = 'vikram'
for x in name:
    print(x.upper())

# range()
# generate a sequnce of numbers
# range(stop)              Starts from 0 to stop-1
# range(strat, stop)       Strats from strat to stop-1
# range(strat, stop, stop) Starts from start to stop-1, incremented
# It does't create a list in memory (unless explicitly converted) but returns a range object thet produces numberson demand


x = 1 
while x <= 5:
    print('Hello world', x)
    x += 1

for i in range(12, 1, -3):  # range[0,1,2,3,4,.....] 
    print("Hello world", i)

print(list(range(10)))

fruits = ["apple", "banana", "cherry", "mango"]
for i in range(len(fruits) -1, -1, -1):
    print(fruits[i])

# enumerate
i = 0
for fruit in fruits:
    print(fruits[i])
    i += 1
print(list(enumerate(fruits)))    

for index, fruit in enumerate(fruits):
    print(fruits[index])

# Break - Immediately exits the loop, regardless of the loop condition  
  
for number in range(10):
    if number == 7:
        break
    print(number)

# continue - Skips the current itertion and moves to the next one.

for number in range(10):
    if number == 7:
        continue
    print(number)

# pass - A do-nothing placeholder. The loop does nothing when pass is hit.

for number in range(10):
    if number == 7:
        pass
    print(number)

for i in range(1, 21):
    if i % 2 == 0:
        print(i, 'even')
    else:
        print(i, 'odd')        

x = 1 #int(input("Enter the number:"))
count = 0
for i in range(1, x + 1):
    if x % i == 0:
        count += 1
if count ==2:
    print('prime')
else:
    print('Not prime')                    

#  for and while loops can have an optional else
#  The else block executes after the loop finishes normally
#  but not if the loop is terminated early with a break statement.   

'''

for item in sequence:
    # Loop body
    if sone_condition
         break  
else:
    # Runs only if the loop was not broken

while condition:
      # Loop body
      if some_condition:
        break
else:
   # Executes if while loop ends without break
                  
'''

nums = [1, 3, 5, 7, 9]
found = False
for num in nums:
    if num % 2 == 0:
       print("Even number found", num)
       found = True 
       break
if not found:
    print("No even numbers found")    


for i in range(1,5):
    print("*" * 6)

print()

for i in range(1,4):
    s = ""
    for j in range(i):
        s += "*"   
        print(s)

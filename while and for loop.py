while loop

count =1
while count <= 5 :
    print('hello')
    count += 1

i = 1
while i <= 5000:
    print("vikram",i) 
    i+=1 

print numbers from 1 to 10
i = 10
while i >=1:
    print(i)
    i -= 1
print('loop ended')    

Q1.print numbers from 1 to 100.
i = 1
while i <= 100:# this is are stoping condition
    print(i)
    i += 1

Q2.print numbers from 100 to 1.
i = 100
while i >= 1:
    print(i)
    i -= 1

Q3.print the mutiplicaton table of a number n.
n = int(input("enter a number:"))
i = 1
while i <= 10:
    print(n*i)
    i += 1

Q4.print the elements of the following list using a loop:
[1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
heroes = ["ironman", "thor", "superman", "batman"]
traverse = ek-ek item par jaana
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

Q5.search for a number x in this tuple using loop:
(1,4,9,16,25,36,49,64,81,100)
nums = (1,4,9,81,16,25,81,36,49,64,81,100)
x = 81
i = 0 #initialization
while i < len(nums):
   if (nums[i] == x):   
      print("found at idx", i)
   else:
      print("finding..")   

   i += 1
 

break   
i = 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i += 1

continue
i = 1
while i <= 10:
    if(i%2 !=0):
        i += 1
        continue #skip
    print(i)
    i += 1


for loop
name = "vikram"
for ch in name :
    if(ch == "r"):
        print("r found")
        if(ch == "i"):
            print("i found")
    print(ch) 
else:
    print("end")

Q6.print the elements of the following list using a loop:
[1,4,9,16,25,36,49,64,81,100]

list =[1,4,9,16,25,36,49,64,81,100]
for nums in list:
    print(nums)       

Q7.search for a number x in this tuple using loop:
[1,4,9,16,25,36,49,64,81,100]       
nums = (1,4,9,16,25,36,49,64,81,25,100,25)
x = 25
idx = 0
for el in nums:
   if(el == x):   
      print("number found at idx", idx)
      break
   idx += 1

Range()

for i in range(10): #range(stop)
   print(i)

for i in range(2,10): #range(start,stop)
   print(i)


for i in range(2,10,2): #range(start,stop,step)
   print(i)

for i in range(2,100,2):
    print(i)

Q8.print numbers from 1 to 100.
for i in range(1,101):
    print(i)

Q9.print numbers from 100 to 1.
for i in range(100,0,-1):
    print(i)

Q10.print the multiplication table of a number n.
n = int(input("enter a number:"))
for i in range(1,11):
    print(n * i)

pass statement

for i in range(17):
    pass
if i > 6:
    pass
print("some useful work")

Q11.WAP to find the sum of first n numbers.(using while)
n = int(input("enter a number:"))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum =",sum)

Q12,WAP to find the factorial of first n numbers.(using for loop)
n = int(input("enter a number:"))
fact = 1

for i in range(1,n+1):
    fact *= i
print("factorial =", fact)    


n = int(input("enter a number:"))
fact = 1
i = 1
for i in range(i,n+1):
    fact *= i
    i += 1
print("factorial =", fact)   

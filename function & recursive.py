Funtion defination

def sum(a,b):
    s = a + b
    return s
print(sum(2,3)) 

def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum
calc_sum(5,3)
calc_sum(6,9)
calc_sum(8,3)

def calc_sum(a,b): #parameters
    return a - b
sum = calc_sum(6235,53653) #function call; arguments
print(sum)

def print_hello():
    print("hello")

print_hello()

#average of 4 numbers
def calc_avg(a,b,c,d):
    sum = a+b+c+c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(4,2,7,2)

built-in function
print()
print("vikramkumar",end="&") #sep = ""
print("golubabu") #end = "\n"

default parameter
def cal_prod(a,b=4):
    print(a+b)
    return a+b
cal_prod(1)

Q1.WAF to print the length of a list.(list is the parameter) 
cities = ["patna","bhubneswar","cuttack","pune","mumbai"]
heroes = ["thor","ironman","captain america","shaktiman"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

Q2.WAF to print the elements of a list in a single line.(list is the parameter)
cities = ["patna", "bhubneswar", "cuttack", "pune", "mumbai"]
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)

Q3.WAF to find the factorial of n.(n is the parameter)
n = int(input('enter a number:'))

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(n)    

Q4.WAF to convert USD to INR.
n = int(input("enter a number:"))
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD",inr_val,"INR")
converter(n)

Q5.WAF to Check Whether a Number is Odd or Even and Return "ODD" or "EVEN"
n = int(input("enter a number:"))
def odd_even(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"
result = odd_even(n)        
print("the number is:",result)     

Recursive Function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("END")
show(3) 

Recursion
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return  fact(n-1)*n
           
print(fact(6))     

Q6.write a recursive function to calculate the sum of first n natural numbers.
num =  int(input("enter the natural number:"))
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n-1) + n
result = sum_natural(num)
print("sum=",result)  

Q7.write a recursive function t0 print all elements in a list.
Hint:use list & index as parameters.
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    else:
        print(list[idx])
        print_list(list,idx+1)
cities = ["patna","delhi","bhubneswar","pune"]
# print_list(cities)        

# Python program to calculate factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# user input
num = int(input("Enter a number: "))

print("Factorial of", num, "is:", factorial(num))

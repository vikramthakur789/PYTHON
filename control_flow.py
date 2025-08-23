# 1. making decisions
# 2. repeating actions
# 3. jumping to different parts of the program

# age = int(input())
# if age >= 18:
#     print("you are an adult.")
#     print("I said you are an adult")
# print("Outside If block")    

temp = 1 #int(input("Temp : "))
is_raining =True # bool(input("Leave Empty: ") ); 
if temp < 10 and  is_raining == True:
    print('wear jacket')

temp = 15
is_snowing = True

if temp < 10:
    print("It's freezing!")
    print("Wear a heavy coat.")
    if is_snowing:
        print("And dont forget your boots!")
print("Have a nice day!")        

money = 400
is_free_popcorn_available = True
if money >= 400:
    print("Movie dekhne gye")
    if(is_free_popcorn_available):
        print("popcorn khane")

score = 54
if score < 60:
    print("Excellent!")
    print("Keep up the good work!")

if score < 60:
    pass
print("You need to study more.")


#else
'''
if condition:
   #code executed when condition is True
else:
   # code executed when condition is false
'''


score = 50
if score >= 35:
    print("Passed")
else:
    print("Failed")
    print("Work hard")    


basket = 19
if basket >= 20:
    print("you win")
else:
    print("Otherwise you will not be able to take the trophy")    
    print("you lost the match")
    
age = 25
if age >= 18:
    print("you can vote.")
else:
    print("you cannot vote yet.")    
     
# password = input("Enter your password:")
#if len(password) >= 6:
   # print("valid password")
#else:
   # print("cannot valid password")         z


age = 8
password = "golu babu" 
if age >= 18:
    if len(password) >= 6:
        print("valid password")
    else:
        print("cannot password")
else:
    print(" I am a kid")  


x = 1 #int(input("Enter the number:"))
if x % 4 == 0:
    print('Even')
else:
    print("odd")                    


'''
if conditionl:
     # Code executed when conditionl is True
etif condition2:
     # Code executed when conditionl is False AND condition2 is True
elif condition3:
    # code executed when conditionl and condition2 are False AND condition3 is True
else:
    # code executed when all conditions are False    
'''

score = 100
if score >= 90:
    grade = "A"  
elif score >= 80:
     grade ="B"
elif score >= 70:
    grade ="C"
elif score >= 60:
    grade ="D"
elif score >= 50:
    grade ="E"  
else:
    grade ="F"    
print(f"Your grade is {grade}")    


temperature = 45
if temperature < 32:
    print("lt's freezing. Wear a heavy coat. ")
elif temperature < 50:
    print("lt's cold. Wear a jacket." )
elif temperature < 70:
    print("cool. Bring a light sweater." )
elif temperature < 85:
    print("lt's warm. T-shirt weather!" )
else:
    print("Its hot! stay hydrated")


number = -10
# 1-9 --> positive single digit
# <=o zero or negative
# >9 --> positive

"""if number > 0:
    print("positive")
elif 0 < number <= 9:
    print("positive single digit")
else:
    print("zero or negative")    

"""
has_fever = True
has_cough = True
has_rash = True

if has_fever:
    print("Take fever medication.")
if has_cough:
    print("Take cough syrup.")
if has_rash:
    print("Apply anti-itch cream.")        


age = 18
income = 50000

if age >= 18:
    print("Adult")
    if income < 30000:
        print("Low income tax bracket")
    elif income < 70000:
        print("Middle income tax bracket") 
    else:
        print("High income tax bracket")
else:
    print("Minor - no income tax")    



x = 1 #int(input())
if x == 5:
    print("x is 5")

# a 6,7,9 —> lucky
# else —> unlucky
a = 99

if a == 6 or a == 7 or a == 9:
    print("lucky")  
else:
    print("umlucky")               

a = 7
if a  in [6,7,9]:
    print("lucky")  
else:
    print("umlucky")               

'''
if condition:
    variable = value if true
else:
   variable = value_if_false

Ternary Operator         
variable = value if true if condition else value if false
'''

age = 65
status = "adult" if age >= 18 else "minor"
print(status)

number = 27
divisor = 6
result = number / divisor if divisor != 0 else "Cannot divisor by zero"
print(result)

if divisor != 0:
    result = number / divisor
else:
    result = " Cannot divisor by zero"    
    print(result)

Operation = input('sub or add ?')
a , b = 5 , 4
result = a + b if Operation == 'add' else a-b if Operation == 'sub' else 'unknon Operation' 
print(result)

num = int(input("Enter any number"))
print('Last digit of number is , num % 10' )

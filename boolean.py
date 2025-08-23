# boolean -> True /False

a = True
b = False
print(type(b))

age = 16
is_adult = age  >= 18
print(is_adult)

# bool is a subclass of int 

print(True == 1)
print(False == 0)
print(True + True)
print(True+False+False-True+10)

print(int(True))
print(int(False))


# truthy or falsy

print(bool("vikram thakur"))
print(bool(None))

# Every Boolean is an integer 
print(isinstance(True, int))
# Intergers are not boolean 
print(isinstance(1,bool))

print(True.bit_length()) #1
print(False.bit_length()) #0  

# has adhaar_card *AND* age >=18 --> DL
has_adhaar = True 
age = 17
print(has_adhaar and age >=18)

# has DL *OR* has adhaar_card --> club
has_dl = True
has_adhaar = False
print(has_dl or has_adhaar)

# *NOT* injury --> play cricket
has_injury = True
print(not has_injury)

'''
| Operator | Meaning                | Example                  |
| -------- | ---------------------- | ------------------------ |
| 'and'    | LOgical AND            | 'True and False'-'False' |
| 'or'     | Logical OR             | 'True or False'-'True'   |
| 'not'    | Logical NOT(negation)  | 'not True' - 'False'     |
'''

x = 5
y = 10
print(x > 3 and y > 8)
print(x > 76 and y > 4)
age = 25
income = 20000
print(age > 18 or income > 400000)
print(age<18 or income >2000)
print(age < 18 or not (income >2000))
# False or True
#Short-circuit Evaluation

# Boolean Operator Precedence
# not > and > or
result = True or False and not True
#        True or False and false
#        True or False
#        True
print(result)

result = (True or False) and (not True)
#        (True or False) and False
#        (True)          and False
#        False
print(result)

age = 25
income = 30000
credit_score = 700
is_eligible = (age >= 20 and age <= 59) and (income > 28000 or credit_score > 650)
print(is_eligible)

working_age = 18 <= age <= 29
# Clearner than (age >= 18 and age <= 29)
print(working_age)

print((not age >= 18) or (not income > 26000))
# False or False

# != == <= >= < > 

text = "Pythyon"
print(text.isalpha)
print(text.startswith("Py"))


language = "python"
#   p     y     t     h     o     n
#  [0]   [1]   [2]   [3]   [4]   [5]- positions/indices


print(language)
print(language[1])
print(1+3)
name1 = "Python" 
name2 = "Python" 
print(name1 == name2)
message = 'Don\'t worry about errors.'
print(message)
dialogue = "She said, \"Python is amazing!\""
print(dialogue)
poem ='''jhhgf jhduiweud uieuioeb uwed  uijiedjjd ,euhiusejhesdjissdih uieed,weiueuiue uieuyeeuie yuievb u9wee euied,
uioerfhfjiefd euiedyhedr jie weui ddui,'''
print(poem)
# C :"\Users\Vipul\Documents"
# directory = "C:\Users\Vipul\Documents"
# print(directory)

print("HEL\"P")
print("HEL\nP")
print("HEL\tP") 


# string concatenation

a = "1"
b = "1"
print(a+b)

first_name = "Golu"
second_name = "Babu"

print(first_name + " " +second_name)

age = 20
message = "My age is " + str(age)
print(message)

city = "Patna"
temp = 38
weather_report = "The temperature in " + city + " is " + str(temp) + " degrees "
print(weather_report)

weather_report = f"The temperature in {city} is {temp*2} degree"
print(weather_report)

a = 89
b = 46
print(f":The sum of {a} and {b} is {a+b}")

name = "vikram"
print(f"first character of {name} is {name[4]}")


# This is a curly brace:{

print(f" This is a curly brace:}}}}")

a = "vikram"
res = a * 4
print(res )

star = "*"
print((star * 8 + "\n") * 9)


a = "python"
print(a*0)
print(a)
print(a * -2)


#pypythonthon
print("py" * 2 + "thon" *2)


#length = len
a="python"
length = len(a)
print(length)

print(len("Hellol\nVikram"))
print(len("❤️"))
print("\u2764")
print("\uFE0F")
print("\u2764\uFE0F")

msg = "Help!"
res = len(msg) <=5
print(res)

print("apple"=="apple")
print('apple'=='vikram')
print("vikram"!="golu babu")
print(1>27)
print(736367<=78788)
print(625>=92)
print(34874<8278823737)
print(36*36)


print("a"<"b")
print('apple'>'Apple')
print(ord('a')) #97
print(ord('A')) #65
print("\u0061")
print(ord('y'))
print(ord('Y'))
print(chr(97))

#   128 character --> ASCII a-z, A-Z, 0-9, punchuation, control



#  string intedxing and slicing
txt = 'PYTHON'
# print (txt[len(txt)]) will give error

print(txt[len(txt) - 3])

#'''
#   string:   P  Y  T  H  O  N
#   Index:    0  1  2  3  4  5
#   Neg Inx: -6 -5 -4 -3 -2 -1
#'''

print(txt[-2])

# string[start:end:step]
# start - inclusive
# end - exclusive


txt = "python programming"
print(txt[0:18])

# P  Y  T  H  O  N     P  R  O   G  R  A  M  M  I  N  G
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 

print(txt[8:18])
print(txt[4:])
print(txt[:])

# gram
print(txt[7:9])
print(txt[-8:-4])

# pto
print(txt[:6:2])

# A negative step traverses the string in reverse direction
print(txt[::-3])

#reverse starting
# gnimmargorp nohtyp

print(txt[::-1])

# string methods


print(txt.upper())
print(txt.lower())
txt = "hello vikram"
print(txt.title())
print(txt.capitalize())

txt = "  hello golu babu  "
print(txt.strip())
print(txt.lstrip())
print(txt.rstrip())

# string.find(substring, start,end)
txt = "Python is amazing, Python is fun"
idx = txt.find("python")
print(idx)
print(txt.find("amazing"))
print(txt.find("is"))
print(txt.find(","))
print(txt.find("Python",19))

 # string.count(substring, start,end)
print(txt.count("is"))

# string.index(substring, start,end)
# the.index() method is similar to .find() but raises a valueerror if the substring is not found.
print(txt.find("java"))
# print(txt.index("java"))
email = "vikramthakurgmail.com"
print(email.find("@") == -1)

# srtring.replace(old, new, count)
txt = "Hello World"
print(txt.replace("World","Python"))
print(txt.replace("World","Python")) # won't work
txt = "banana banana banana"
print(txt.replace("banana","mango",1))

text1 = 'Python'
text2 = 'Python3'
print(text1.isalpha())  #True
print(text2.isalpha())  #False
print(text1.isalnum())
print(text2.isalnum())
text1 = "32456"
text2 = "6047Golu babu"

print(text1.isdigit())
print(text2.isdigit())

# islower(). isupper()
text = "  \n\t  "
print(text.isspace())

# startswith endswith
text = 'Python is amazing'
print(text.startswith("Python")) #True
print(text.startswith("is"))     #False
print(text.endswith("amazing"))  #True
print(text.endswith("Python"))   #False
print(text.endswith("is",0,9))   #True

text = "apple,banana,mango,orange,"
print(text.split(" "))
sentence = "Python is fun to learn"
print(sentence.split(","))
li = ['apple', 'banana','orange','grape']
print(" " . join(li))


# .format(Method)
name = "vikram"
goal = "software engineer"
message = " Hello, my mame is {} and my goal is {} amd my age is {} ".format(name,goal,20)
print(message)
message = "Hello, my mame is {p1} and my goal is {p2} amd my age is {p3}". format(p1=name,p2=goal,p3=20)
print(message)

# Old-style formatting with % operator
# "string with format specifier" % values

name = "Alice"
greeting = "Hello, %s!" % name 
print(greeting)

'''
%s— String (or any object with a string representation)
%d - Integer
%f — Float
%x- Hexadecimal
%0— Octal
%.2f - Float with precision (2 decimal places in this example)
'''
age = 20
message = "I am %d years old." % age
print(message)

name = "golu"
age = 20
message = " I am %d years old and My name is %s." % (age,name)
print(message)

pi = 3.14159265359
print("Pi rounded to 2 decimal places: %.8f" % pi)

# String Immutability

s = "Hello"
print(s[0])
# s[0] = "M" wont work
print("M" + s[1:])
s = "M" + s[1:]
print(id(s))

# Raw Strings
rs = r"He\nllo"
print(rs)
print(r"ioeeryudiueehewjiwer\dfbhiorf iorueirr")

r"She said, \"Hello\""  # works: backslash escapes the quote
r" This ends with a \\" # Works
r" This ends with a \"" # Works
# r"She said,"Hello""     # SyntaxError: quote ends the string too
# r"This ends with a \\\" # syntax error 
# r"This ends with a \"   # syntax error

# odd \ -—> escape closing quote
# even \ ——> doesn't escape closing quote

# Question 
# 1. string method chaining
#strip, capitalize the first latter of each word, and replace "skill" with "Expertise"
text = " python programming SKILLS"
text = text.strip()
text = text.title()
text = text.replace("skills","Expertise")
print(text)
print(text.strip().title().replace("skills","Expertlise"))

# 2. advanced slicing challenge
# Print every second character using slicing
# Print the string in reverse order using slicing
# Extract and print just using negative indices
s="Python Programming Language"
print(s[::2])
print(s[::-1])
print(s[-21:-9])

# 3. String Concatenation and Slicing
# create a new string by extraction the first letter of each word and concatenating them 
text = "python is easy to learn"
result = text[0] + text[7] + text[10] + text[15] + text[18]
print(result)

# 4. String Palindrome Check
# pop, radar
word1 = "radar"
word2 = "pop"
print(word1,word2)
print(word1==word2)
word = "radar"
print(word == word[::-1])

#5.
text = "mississippi"
# Find count occurrences of 'i' , 's', 'p', and 'm'
count_i = text.count("i")
count_s = text.count('s')
count_p = text.count("p")
count_m = text.count('m')


print(f"i:{count_i}")
print(f's:{count_s}')
print(f"p:{count_p}")
print(f"m:{count_m}")

a = int(input("enter the first num:"))
b = int(input("enter the second num:"))
c = int(input("enter the third num:"))
d = int(input("enter the fourth num:"))
if(a >= b and a >= c):
    print("first num is largest",a)
elif(b >= c and b >= d):
    print("second num is largest",b)
elif(c >= d):
    print("third num is largest",c)
else:
    print("fourth num is largest",d)            

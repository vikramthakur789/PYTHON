# positive, negative, or zero
a = 48
b = -23
c = -28
print(a,b,c) 

# python integers have unlimited precision

salary = 10_00_000
print(salary)
binary_num = 0b101010
print(type(binary_num))
print(binary_num)
a = 10
b = 3
print(f"Addition: {a+b}")
print(f"substracion:{a-b}")
print(f"multiplication:pri{a*b}")
print(f"divion:{a / b}")
print(f"regular divion:{a / b}")
print(f"integer divion:{a / b}")
print(f"power:{a**b}")
print(f"modules:{a%b}")
print(f"negation:{a} = {-a}")
print(f"absolute value of {b} - {a} = {abs(b-a)}")
result = 3+5-3%32*23
print(result)

# () > ** > *,/,//,% > +,-
result = 10-(2**3)//2+7
print(result)

x = 10
y = 6

# Bitwise AND & 
bitwise_and = x & y
print(f"{x} & {y} = {bitwise_and}")

# Bitwise OR |
bitwise_or =x | y
print(f"{x} | {y} = {bitwise_or}")
print(0b1110)

# Bitwise XOR
bitwise_XOR = x ^ y
print(f"{x} ^ {y} = {bitwise_XOR}")
print(0b1100)

# Bitwise NOT 
bitwise_not = ~x 
print(f"Binary of {x} is {bin(x)}") # 1010
print(f"~{x} = {bitwise_not}")

# Left shift
left_shift = x << 1
print(f"{x} << 1 = {left_shift}")
print(0b10100)
print(0b011)

# return largest integr less than or equal to the exat division
print(10//3)
print(10.0//3)
print(-10//3)
print(10//-3)


# Assignment Operators

x = 1
name = "Vipul"
# LHS = RHS
#LHS must be a valid variable name
#RHS can be any expression that produces a value

#x =int(input("x ki value daliye: "))
#y = int(input("y ki value daliye: "))
x = 1
y = 2
x,y = y,x
print(x , y)

z = 3
z = z+6
print(z)

v = 327
v*= 6 #v*=6,v=v*6
print(v)

msg = "Hello"
msg+= " golu babu"
print(msg)

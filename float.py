# typically 15-17 significant digits
salary = 2.345
v = -7.445
x = - .234
print(v,x)

a = 437.5867
print(type(a))

b = 9/2
v = float(2)
print(v)

t = int(354.72)
print(t)

result = 0.4 + 0.2543
print(result)

electron_mass = 9.11e-25 # 9.11 x 10^-25
result1 = 4e25 * 5e3
print(result1)

a = 1500.0
b = 1.5e3
print(a == b)

very_large = 10000000000000000.0
print(very_large)

very_small = 0.00000000000000001
print(very_small)
  
pos_infinity = float('-inf')
print(pos_infinity)
pi = 4.746238787234
print(f"{pi:.4f}")  

a = 0.3
b = 0.1 + 0.2
print(a)
print(b)
print(a == b)

import math
print(math.isclose(a,b))

import decimal 
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
print(a + b)

pi = 4.74
print(round(pi,3))
print(f"{pi:.3f}") 
 

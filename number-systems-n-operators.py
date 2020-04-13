import os
import math

a = 2+2
print(a)

b = 4*4
print(b)

# Division

c = 5/3
print(c)

print(type(c))

# FLOOR Division -- Just gives the integer value ( Divisor)

e = 7//3
print(e) # O/P = 2
print(type(e))

# Modulo Operator - Remainder value ; 
# Use this to do - Even or Odd check;

f = 5 % 3
print(f) # O/P = 2

# Exponent - **

g = 4**3
print(g) # O/P = 64

########## NUMBER SYSTEMS ##########

# Decimal - base 10, Binary - base 2 etc.. 

# Represting these number system in Python: 

# Binary - Prefix 0b - 0b0001 ( For 1)
# Octal - Prefix 0o (zero-o) - 0o0001 ( For 1 )
# Hexadecimal - Prefix 0x - 0xFF012

# Example - Converting 15 to Binary and back to Decimal

# Print binary format of 10

x = bin(10)
print(x) # O/P : 0b1010

y = oct (59)
print(y) # O/P: 0o73

z = hex (1024)
print(z) # O/P: 0x400

######################## FLOATING POINT ACCURACY ##########

float_x = 0.1
print(float_x)

abc = (math.pi)
print (abc) # O/P: 3.141592653589793

abc_a = format(math.pi, '.6g') # Gives 6 significant digits
print(abc_a) # O/P: 3.14159

abc_b=repr(math.pi) # repr() - Return a string containing a printable representation of an object
print(abc_b) # O/P: 3.141592653589793




































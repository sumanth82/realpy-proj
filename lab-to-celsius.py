#!/usr/bin/env python3.7
import os

x = input('What temp (in Fahrenheit) would you like converted to celsius?')
print(type(x))
print(x)

y = (int(x) - 32 ) / ( 9/5 ) # O/P: 32.22222222222222

z = round(y, 2)

print( "Fahrenheit", x, "is", z, "celsius rounded to 2")







# Thsi script should do the following:
# Will take the input from the user, print the following information about the user provided message:

#The first character
#The last character
#The middle character (for even length strings we'll return the integer just after the exact center).
#Every even index character
#Every odd index character
#The message in reverse

import os

x = input('The sample word for indexing and slicing is: ')
print(x)

#The first character

a = x[0]
print(a)

#The last character

b = x[-1]
print(b)

#Every even index character

c=x[0:-1:2]
print(c)

#Every odd index character

d=x[1:-1:2]
print(d)

#The message in reverse

e=x[::-1]
print(e)

#The middle character (for even length strings we'll return the integer just after the exact center).

f = len(x)
print(f)

g = int(len(x)/2)
print(g)

h=x[g]
#h=x[(int(len(x))/2)]
print(h)








# bitwise and unary operators
# Unary operator - Just has 1 operand; E.g: ~1 ( complement of 1)

a = 0b010
print(a) # O/P: 2

print(bin(a)) # O/P: 0b10

print(~a) # complement of a ((value of a * -1) -1)

# O/P: -3 ( (value of a * -1) -1)

# AND, OR, XOR, NOT

a = 0b0010
b = 0b0101

print(bin(a|b)) # O/P: 0b111

print (bin(a&b)) # O/P:0b0

print (bin( a ^ b )) # O/P: 0b0111

####

## left-shift and right-shift ##

##  >>  --> RIGHT SHIFT
##  <<  --> LEFT SHIFT

a = 0b110

print(bin( a >> 2 ))  # O/P: 0b1 --> RIGHT SHIFT truncates the right 2 char;
print(bin(a << 2)) # O/P: 0b11000 --> LEFT SHIFT adds 2 0's (padding) at the end; 

##### BOOLEAN OPERATORS - Represented in words #####

print(not True) # O/P: False
print(not False) # O/P: True

print(True or False) # O/P: True

print(True and True) # O/P: True

print(True and False) # O/P: False

#################

print(1 < 2) # O/P: True

print (2.0 > 3) # O/P: False

##### COMPARISON OPERATORS #####

xyz = ('a' > 'b')
print(xyz) # O/P: False

tmt = ('b' > 'a') 
print(tmt) # O/P: True

print(a>b) # O/P: 


### HOW TO Get the value of a string a? Use - ord() built-in function

print(ord('a')) # O/P: 97
print(ord('b')) # O/P: 98 ; Hence 'b' > 'a'

####

##### integer comparison 

print( 1 == 1) # O/P: True
print ( 1 != 1) # O/P : False

### Identity operator

print(1 is 1) # O/P: True
print(2 is 1) # O/P: False
print(2 is not 1) # O/P: True

print(id('a')) # O/P: 4565967984
print(id('a')) # O/P: 4565967984

### Empty list - []

########## OPERATOR PRIORITY or Binding ##########

# 1st priority in evaluation is - (), [], {} etc.. 
# 2nd priority is based on Math evaluation 

test_num= 14 & 3 * 2 + 4 ## 14 bitwise AND ( 3*2+4 )
print(test_num) # O/P: 10

a = bin(14)
print(a)

b=bin(10)
print(b)
























































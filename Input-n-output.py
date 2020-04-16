### INPUT and OUTPUT OPERATIONS
## Typecasting ## Move the object from one type to another;

x = 1
print(x)

y = 2
print(float(y)) # O/P: 2.0

z=1.5
print(int(z)) # O/P: 1

print(str('1'))
print(str('1.0'))

#### Boolean ##

print(bool(1)) # O/P: True
print(bool(2.4)) # O/P: True

print(bool(0)) # O/P: False
print(bool(0.0)) # O/P: False

print(bool(-1.10)) # O/P: True

##### 

print(('This' and 'That')) # O/P: That ( compares each character one by one - basically a boolean on each character )
print('1' or '0' or '2')

print(not(1)) # O/P: False

###############   INPUT FUNCTION and PRINT FUNCTION - User Input ####################

x = input()  # Waits for user-input
print(x)

fav_color = input("Favorite Color is:")
print(fav_color)


### 

name = input("What is your name? ")
color = input("What is your fav color? ")
age = int(input("What's your age? "))

print(name)
print("is " + str(age) + " years old")
print("His favorite color is" + color + ".")

# O/P:

#pinkk
#is 7 years old
#His favorite color isk.

print(name, end= " ")
print("is " + str(age) + " years old", end = " ")

#O/P:
# z is 8 years old // (All in single line)

print(name, 'is', age, 'years old and loves the color', color + '.', sep=" #", end="\t") # sep = separator

# O/P: sam #is #38 #years old and loves the color #pink.

print(name)











## By default, end of a print statement is \n; So instead you can change with print(name, end = " ") 






# SYNTAX:
# while CONDITION:
#    print(xxxx)

# For an infinite loop run the below command:
#while (1<2):
#    print("Hello world")

count = 0
while(count <=4):
    print('Python for real this time')
    count+=1
# Prints the output 5 times

######  FOR LOOP
#SYNTAX:

#for TEMP_VARIABLE in SEQUENCE ( a list or a tuple):
#    print(xxxx)

colors = ['blue', 'pink', 'red', 'orange']

for color in colors:
    print(color)

# O/P:  

#blue
#pink
#red
#orange

ages = {'Kevin': 59, 'Bob': 69, 'Rob': 79}

for age in ages:
    print(age)

# O/P:
#Kevin
#Bob
#Rob

for key, value in ages.items():
    print(key, value)

# O/P:
#Kevin 59
#Bob 69
#Rob 79

for letter in 'my_string':
    print(letter)

# O/P:

#m
#y
#_
#s
#t
#r
#i
#n
#g

################  NESTING LOOPS and CONDITIONALS


counter = 0

while counter <=25:
    if counter % 4 == 0:
        print(counter)
    counter+=1

# P.S: Important to maintain the index!!!!!!  
# O/P: 

#0
#4
#8
#12
#16
#20
#24

####### Control Loop execution with BREAK and CONTINUE #####

# Print an odd number;

count = 0

while count < 10:
    if count % 2 == 0:
        count+=1
        continue # If condition met get out of if loop to the next statement 
    print(f"The count value is: {count}")
    count+=1

# O/P: 

#The count value is: 1
#The count value is: 3
#The count value is: 5
#The count value is: 7
#The count value is: 9

### BREAK - Totally ends the loop or a context if condition met;

count = 1

while count <= 10:
    if count % 2 == 0:
        break
    else:
        print("Some value")
        count+=1
print(f"The odd number in question is: {count}")

#### Integrating 'else' with Loops #####

count = 1

while count <=4:
    print(f"The value of count is {count}")
    count+=1
else:
    print("The loop is complete")

## You will need an else statement followed by a break usually #####

######## RANGE ##### 

# range is light-weight, takes up small space
# Format:

# range(<start_no>, <stop_no>, <step_no>)
# range(<stop_no>)

my_range = range(10)
print(my_range) # O/P: range(0, 10)

print(type(my_range)) # O/P: <class 'range'>

print(list(my_range)) #O/P: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_range = list(range(1, 14, 3))

print(list_of_range) # O/P: [1, 4, 7, 10, 13]

# Use range instead of while loop to iterate and generate a list of long sequence 

#########  LIST COMPREHENSIONS #####

colors = ['red', 'green', 'blue', 'orange']

for color in colors:
    if color == 'blue':
        print(f"The color we always wanted is: {color}")
        break
    else:
        print(f"The choice of color we got is: {color}")
        
colors = ['red', 'green', 'blue', 'orange']

uppercase_colors = []

for color in colors:
    uppercase_colors.append(color.upper())

print(uppercase_colors)

# O/P: ['RED', 'GREEN', 'BLUE', 'ORANGE']

colors = ['pink', 'purple', 'white', 'black']
uppercase_colors = [color.upper() for color in colors] # This is list comprehension 

# In a List, use the first entry for the new values, second entry to run the for loop and feed the first entry
# Mainly used for filtering 

print(uppercase_colors)


names = ['mushika', 'spider', 'aarush']

warm_names = [name for name in names if name in ['mushika', 'spider'] ]

# Single line list comprehension which includes a for loop and if conditional 
 
print(warm_names)
 #O/P: ['mushika', 'spider']

 


























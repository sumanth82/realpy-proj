# Generators are like range() that can be used within a function
# key thing in a generator function is yield within the function defn.
# yield --> is like return but once it returns it STOPS the function exec. 
# Use next() function to fetch the value of the iterator 
# Instead of for within a function, you can use thus gen_range()

# Syntax: 
# def gen_range(<stop>, <start=1>, <step=1>):


def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num+= step

generator = gen_range(6)
print(generator) 

# O/P: <generator object gen_func at 0x109025450>
# Returns the generator object;
# To get the objects from the generator function, use the next() function

print(next(generator))

# O/P: 1

# use python3 -i generator.py to run interactively 
# Then run next(generator)
# It keeps iterating and returns the value till the end of stop value 

for num in gen_range(10, step=2):
    print(num)

# O/P: 1
#3
#5
#7
#9


######################## 

# Generators are functions that behave like iterators and hence can be used as lists

def gen_range(stop, start=1, step=1):
    num = 1
    while num <= stop:
        yield num
        num+=1 

generator= gen_range(6)

print(generator)

# O/P: <generator object gen_range at 0x1033284d0>

print(next(generator))

# O/P: 1

# If you run the program using -i option and run  next(generator) function, it keeps incremeting
# and returns the output like 2, 3 and so on.. 

print(list(generator))

# O/P: [2, 3, 4, 5, 6]





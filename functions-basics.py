##

######   FUNCTION FORMAT ##### 
# def <function_name_in_snake_casing>(<parameter_1>, <parameter_2>):

def print_something(something):
    pass


# step 1: Define a function
def print_name(name):
    print(f"Name is {name}") # This just writes out to the screen but doesn't return any value that can be used in a variable 

# step 2: Call a function 
print_name("Keith")
 
# Define a function with a return statement (i.e. output of a function that can be used
# in a variable)

def test_num(num):
    return num + 2

result = test_num(2)

print(result)

# O/P: 4


#####################################

def contact_card(name, age, car_model):
    return print(f"{name} is the buyer and his age is {age} with the model {car_model}") 

contact_card("Keith", 29, "Honda Civic")

## Other way of passing the values to the parameters using keyword-arguments

def contact_info(name, luxury_car):
    return print(f"{name} is the buyer and wants {luxury_car}")

contact_info(name="Edward", luxury_car="Mercedes Benz S500")

#### Another way of passing the keyword-arguments value
# In arguments, you can pass a default value 

def can_drive(age, driving_age=16):
    return print(age < driving_age)

can_drive(19)

# O/P: True 

##### RECURSION - Define a function and call a function from within the function defn ##########

# fibonacci series - start with 1, add 1 with previous number to get next number;
# 1, 1, 2, 3, 5, 8, 13 .. 

# If you need the nth no. you need to do a (n-2) + (n-1), the last 2 essentially being the indexes.

#f(n) = f(n-2) + f(n-1)

# f(5) = f(3) + f(4)
# f(8) = f(6) + f(7)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n-2) + fib(n-1)

item_to_calc = int(input("What Fibonacci item would you like to calculate? "))
print(fib(item_to_calc))







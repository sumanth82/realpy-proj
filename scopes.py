if 1 < 2:
    x = 5

while x < 6:
    print(x)
    x+=1

print(x)

# O/P: 5, 6

# Conditionals and Loops do not have any scopes defined in them
# However a variable defined within a function has it's scope set to that function den ONLY.

y = 5

def set_x(y):
    print("Inner y:", y)
    x = y
    y = x

set_x(10)

print(f"Outer y is {y}")


# NOTE: Use the keyword 'global' within a func defn for a variable defined outside the func
# and ref that value within the func and as well outside the func

a = 10

def test_word(y):
    print(f"The value of y is: {y}")
    x = a
    print(x)
    
    global z
    z = '10'

test_word(200)

print(f"The value of z is: {z}")
print(f"The value of x is: {x}")





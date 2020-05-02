# Tuples = IMMUTABLE
# Tuple MUST end with a ,

point=(2.0, 3.0)
print(point)

#point[1]=1
#print(point[1]) # Fails with error - TypeError: 'tuple' object does not support item assignment

point_3d=point + (4.0,)
print(point_3d) # O/P: (2.0, 3.0, 4.0)

# For Individual object within a tuple re-assignment

x,y,z=point_3d

print(x) # O/P: 2.0
print(y) # O/P: 3.0
print(z) # O/P: 4.0

# Unpacking

print("My name is: %s %s" %('Sumant', 'Renukarya'))

# O/P: My name is: Sumant Renukarya


##


my_list = [1,2,3]
my_tuples=(my_list, 10,20,30)
print(my_tuples) # O/P: ([1, 2, 3], 10, 20, 30)

other_list=['x', 'y', my_tuples]
print(other_list) # O/P: ['x', 'y', ([1, 2, 3], 10, 20, 30)]














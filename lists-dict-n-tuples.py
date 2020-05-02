# LISTS - ARE MUTANLE OBJECTS unlike STRINGS:

my_list = [1,2,3,4,5]
print("This list is", my_list)

print("This list is", my_list[0])

mixed_list=['a',1, 'sumant', 3.0]
print("Mixed list is:", mixed_list)

print(len(mixed_list))

## REPOSITIONING THE STRINGS in a LIST

sample_list=['a', 'e', 'i', 'o', 'u']
print(sample_list)

sample_list[3:]=[]
print(sample_list)

# Change the value of string in index 0 to z

sample_list[0]='z' 
print(sample_list) # O/P: ['z', 'e', 'i', 'o', 'u']

# CONCATENATE the LIST:

my_string = sample_list + ['a', 'aa', 'e', 'ee']
print(my_string) # O/P: ['z', 'e', 'i', 'a', 'aa', 'e', 'ee']

# delete a LIST using del statement

del my_string[0]
print(my_string)

# LIST FUNCTIONS and METHODS:

my_list = [1, 2, 3]
my_list+=[4,5,6]
print(my_list)

my_list.append(7)
print(my_list)

# my_list.insert(<index_position>, object) ; It basically appends does not replace

my_list.insert(7, 10)
print(my_list)

# TO know the position of an item in the list - use index() method
# my_list.index(<object_in_list>)

print(my_list.index(10)) # O/P: 7

my_list=[1, 2, 3]
y = 4 in my_list # Like asking a question; Is object 4 in my list; O/P = False
print(y) # O/P: False

x = 4 not in my_list 
print(x) # O/P: True


# SORTING a list - Used sorted() function

test_list = [1, 5, 2, 7, 3, 9]
print(sorted(test_list))

# REVERSING a list - Use reversed() function

print(reversed(test_list)) # O/P: <list_reverseiterator object at 0x10be3efd0>
print(list(reversed(test_list))) # O/P: [9, 3, 7, 2, 5, 1]

print(list(reversed(sorted(test_list))))  # O/P: [9, 3, 7, 2, 5, 1]

# NESTED lists - Matrices and Cubes;

a = [[1,2,3], [4,5,6]] # This represents a matrix
print(a)

# To get the row count:

row_count= len(a)
print(row_count) # O/P: 2

column_count = len(a[0]) # Length of the first object in the list; 
print(column_count) # O/P: 3

test_column_count=len(a[1])
print(test_column_count) # O/P : 3

print(a[0][0]) # O/P: 1
print(a[0][1]) # O/P: 2
print(a[1][0]) # O/P: 4











































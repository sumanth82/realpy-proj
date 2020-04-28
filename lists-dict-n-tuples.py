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

















test_str = 'testing'
y = test_str.capitalize()
print(y) # O/P: Testing

# Any created string is immutable and can be verified using - id('<string>')
# len 

len('hello') # O/P: 5

## STRING INDEXING and SLICING:

test_str = 'python'
print(test_str[0]) # O/P: p
print(len(test_str)-1) # O/P: 5

test_str0 = test_str[len(test_str) - 1] # Get the index value of the last char in a string

print(test_str0) # O/P: n  # p y t h o n
                             #-6 -5 -4  -3 -2 -1

test_str1=test_str[-1]
print(test_str1) # O/P = n; Prints the last digit

## SLICING:

a = 'SUMANT'
b = a[0:4]
print(b) # O/P: SUMA

c=a[1:6:2] # slicing 1 to 6 and step by 2

print(c) # O/P: UAT

# REVERSE a STRING

c=a[::-1] # This says starting index is the beginning of the string, ending index is the end of the string, slice from last to first
print(c)  # O/P: TNAMUS





















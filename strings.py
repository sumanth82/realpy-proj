##### STRINGS ENCODINGS and FUNCTIONS #####
# Default encoding for a string is Unicode and particularly - UTF-8

a = 'test'
print(a) # O/P: test
print(type(a)) # O/P: <class 'str'>

print(ord('x')) # O/P 120 - represents unicode code point 

# Every individual car has access to it's individual code point 
# UTF - Unicode Transformation Format - Stored in 8 bits; 
# # UTF-8 can hold upto a million code points

print(ord('™')) # In Mac - press option and 2 

# O/P: 8482

# ASCII - Can only handle letters, numbers and common punctuation formats and can hold only upto 256 code points 
# First 128 code points of ASCII are valid in UTF-8 as well

print(chr(8482)) # O/P: ™

#######################  STRING METHODS - lower(), upper(), capitalize(), title(). is() ##########


sample_str = " THIS can NOT be True!!"

print(sample_str)

print(sample_str.lower())
print(sample_str.upper())

sample_word = 'sumant'
print(sample_word.capitalize()) # Just capitalizes the FIRST letter and lowers the other 

# O/P: Sumant

print(sample_str.title()) # Capitalizes first letter in each word in a sentence.

# O/P: This Can Not Be True!!

print(sample_word.isascii())

# O/P: True

print(sample_word.islower())

#O/P: True

print(sample_word.isupper())

# O/P: False

print(sample_str.title().istitle()) # Convert a string to a tile and check if it is a title

# O/P: True

print(sample_word.isspace())

# O/P: False

print('1.0'.isdecimal()) # O/P: False
print('1'.isdecimal()) # O/P: True

print('1'.isdigit()) # O/P: True
print('11'.isnumeric()) # O/P: True


#####  ALPHABETICAL ####

sample_str = 'Timon'
print(sample_str.isalpha()) # O/P: True

sample_str1 = 'ka17'
print(sample_str1.isalnum()) # O/P: True

print('1bear'.isidentifier()) # O/P: False

print('This'.isprintable()) # O/P: True

##### PART 2 - split(), join(), #####
## SPLIT 

phrase = 'Take life 30 mins at a time'

print(phrase.split())
# O/P: ['Take', 'life', '30', 'mins', 'at', 'a', 'time']
print(type(phrase.split())) # <class 'list'>

test_url = 'https://example.com/users/jimmy'
users = test_url.split('/')[-1]
print(users) # O/P: jimmy

web_url = 'https://sample.com/places/ckm'

place = web_url.split('/') # Says - split at '/'
print(place)
# O/P: ['https:', '', 'sample.com', 'places', 'ckm']

print(place[-1])
# O/P: ckm

new_str = "This in a given scenario is incorrect"
print(", ".join(new_str))
# O/P: T, h, i, s,  , i, n,  , a,  , g, i, v, e, n,  , s, c, e, n, a, r, i, o,  , i, s,  , i, n, c, o, r, r, e, c, t

sample_test = ['First line', 'second line', 'Third line']

print("\n".join(sample_test))

# O/P: 

#First line
#second line
#Third line

####################  .format() method #############

template = "Hello, My Name is {}, and I really enjoy {}, and hope life gets back to normalcy in 2022"
print(template)

print(template.format('Timon', 'Yoga'))
# O/P: Hello, My Name is Timon, and I really enjoy Yoga, and hope life gets back to normalcy in 2022

print("For a guy who never was a {0}, this specific {1}, is very interesting".format('Full-Time Programmer', 'Python course'))

# O/P: For a guy who never was a Full-Time Programmer, this specific Python course, is very interesting

#####

















































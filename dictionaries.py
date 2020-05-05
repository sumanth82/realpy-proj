# Dict start with a {} and MUST be key:value pairs
# Keys must be immutable and MUST be UNIQUE in a dict. 
# Dict themseleves are mutable types, just like lists

ages = {'Kevin': 59, 'alex': 29, 'Bob': 40}
print(ages)

# O/P: {'Kevin': 59, 'alex': 29, 'Bob': 40}

print(ages['Kevin'])
# O/P: 59

# Add new object to the ages dict:

ages['Kayla']=21
print(ages)

# O/P: {'Kevin': 59, 'alex': 29, 'Bob': 40, 'Kayla': 21}

# Modify the existing value in a specific key

ages['Kevin'] = 70
print(ages)

# O/P: {'Kevin': 70, 'alex': 29, 'Bob': 40, 'Kayla': 21}
# TO delete a DICT object

del ages['alex']
print(ages)

# O/P: {'Kevin': 70, 'Bob': 40, 'Kayla': 21}

print('Kevin' in ages) # O/P : True

# dict () is the official class

weights = dict(subaru='silver', honda='maroon')
print(weights)

# O/P: {'subaru': 'silver', 'honda': 'maroon'}

###### DICT METHODS - keys(), values(), items()

ages = {'Pruthvi': 50, 'Sandeep': 40}
print(ages)

z = ages['Pruthvi']
print(z) # O/P: 50

print(ages.keys()) # dict_keys(['Pruthvi', 'Sandeep'])
print(list(ages.keys())) # ['Pruthvi', 'Sandeep']


print(ages.values()) # dict_values([50, 40])
print(list(ages.values())) # [50, 40]

print(ages.items()) # dict_items([('Pruthvi', 50), ('Sandeep', 40)]) - Gives a tuples of the key-value pair of the dict
print(list(ages.items())) # [('Pruthvi', 50), ('Sandeep', 40)]



























